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

    def set_system_policies(self, disable: bool):
        """Enable or disable various Windows system policies."""
        if platform.system().lower() == "windows":
            try:
                value = 1 if disable else 0
                # Policies\System
                sys_key_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
                sys_key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, sys_key_path, 0, winreg.KEY_SET_VALUE | winreg.KEY_WOW64_64KEY)
                winreg.SetValueEx(sys_key, "DisableTaskMgr", 0, winreg.REG_DWORD, value)
                winreg.SetValueEx(sys_key, "DisableRegistryTools", 0, winreg.REG_DWORD, value)
                winreg.SetValueEx(sys_key, "DisableLockWorkstation", 0, winreg.REG_DWORD, value)
                winreg.CloseKey(sys_key)
                
                # Policies\Explorer
                exp_key_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"
                exp_key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, exp_key_path, 0, winreg.KEY_SET_VALUE | winreg.KEY_WOW64_64KEY)
                winreg.SetValueEx(exp_key, "NoControlPanel", 0, winreg.REG_DWORD, value)
                winreg.CloseKey(exp_key)

                # Policies\Microsoft\Windows\System for CMD
                cmd_key_path = r"Software\Policies\Microsoft\Windows\System"
                cmd_key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, cmd_key_path, 0, winreg.KEY_SET_VALUE | winreg.KEY_WOW64_64KEY)
                # 1 blocks cmd and batch
                winreg.SetValueEx(cmd_key, "DisableCMD", 0, winreg.REG_DWORD, value)
                winreg.CloseKey(cmd_key)

                action = "Disabled" if disable else "Enabled"
                self.logger.log_activity("SYSTEM_LOCKDOWN", f"System Policies {action} via Registry")
                return True
            except Exception as e:
                self.logger.log_activity("SYSTEM_ERROR", f"Failed to modify system policies: {e}")
                return False
        return False

    def prevent_system_sleep(self, prevent: bool):
        """Prevent or allow the system to sleep/turn off display."""
        if platform.system().lower() == "windows":
            try:
                ES_CONTINUOUS = 0x80000000
                ES_SYSTEM_REQUIRED = 0x00000001
                ES_DISPLAY_REQUIRED = 0x00000002
                
                if prevent:
                    # Prevent sleep and display turn off
                    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)
                    self.logger.log_activity("SYSTEM_LOCKDOWN", "Preventing system sleep and display off")
                else:
                    # Allow sleep
                    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
                    self.logger.log_activity("SYSTEM_LOCKDOWN", "Allowed system sleep")
                return True
            except Exception as e:
                self.logger.log_activity("SYSTEM_ERROR", f"Failed to set thread execution state: {e}")
                return False
        return False
