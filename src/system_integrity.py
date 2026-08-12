import platform
import subprocess
import os
import ctypes

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
