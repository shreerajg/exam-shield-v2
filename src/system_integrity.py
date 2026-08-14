import platform
import subprocess
import os
import ctypes
import winreg

class SystemIntegrityManager:
    def __init__(self, logger):
        self.logger = logger

    def is_running_in_vm(self):
        """Detect if the system is running inside a Virtual Machine."""
        if platform.system().lower() != "windows":
            return False
            
        vm_indicators = ["vbox", "vmware", "virtual", "qemu", "kvm", "hyper-v"]
        
        # Check baseboard
        try:
            output = subprocess.check_output(["wmic", "baseboard", "get", "manufacturer,product"], text=True).lower()
            for indicator in vm_indicators:
                if indicator in output:
                    return True, f"Baseboard VM Match: {indicator}"
        except Exception:
            pass
            
        # Check computer system
        try:
            output = subprocess.check_output(["wmic", "computersystem", "get", "model"], text=True).lower()
            for indicator in vm_indicators:
                if indicator in output:
                    return True, f"System Model VM Match: {indicator}"
        except Exception:
            pass
            
        return False, "Native"

    def clear_clipboard(self):
        """Clear the system clipboard on Windows to prevent pasting stored answers/content."""
        if platform.system().lower() == "windows":
            try:
                if ctypes.windll.user32.OpenClipboard(None):
                    ctypes.windll.user32.EmptyClipboard()
                    ctypes.windll.user32.CloseClipboard()
            except Exception as e:
                try:
                    os.system("echo off | clip")
                except:
                    pass

    def is_debugger_present(self):
        """Detect if the system is being debugged."""
        if platform.system().lower() == "windows":
            try:
                if ctypes.windll.kernel32.IsDebuggerPresent():
                    return True
            except Exception:
                pass
        return False

    def get_monitor_count(self):
        """Get the number of connected monitors."""
        if platform.system().lower() == "windows":
            try:
                return ctypes.windll.user32.GetSystemMetrics(80)  # SM_CMONITORS
            except Exception as e:
                self.logger.log_activity("SYSTEM_ERROR", f"Failed to get monitor count: {e}")
        return 1

    def get_connected_usb_drives(self):
        """Get a list of connected USB drive letters."""
        if platform.system().lower() == "windows":
            try:
                # DriveType 2 means Removable Disk (USB, Flash Drive, etc.)
                # Use CREATE_NO_WINDOW to avoid flashing console
                output = subprocess.check_output(
                    ["wmic", "logicaldisk", "where", "drivetype=2", "get", "deviceid"],
                    text=True, creationflags=subprocess.CREATE_NO_WINDOW
                )
                # Parse output, ignore the header "DeviceID" and empty lines
                drives = [line.strip() for line in output.split('\n') if line.strip() and "DeviceID" not in line]
                return drives
            except Exception as e:
                self.logger.log_activity("SYSTEM_ERROR", f"Failed to get USB drives: {e}")
        return []

    def set_task_manager_disabled(self, disable: bool):
        """Enable or disable Task Manager via Windows Registry."""
        if platform.system().lower() == "windows":
            try:
                key_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
                # Open or create the key
                key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE | winreg.KEY_WOW64_64KEY)
                value = 1 if disable else 0
                winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, value)
                winreg.CloseKey(key)
                action = "Disabled" if disable else "Enabled"
                self.logger.log_activity("SYSTEM_LOCKDOWN", f"Task Manager {action} via Registry")
                return True
            except Exception as e:
                self.logger.log_activity("SYSTEM_ERROR", f"Failed to modify Task Manager policy: {e}")
                return False
        return False
