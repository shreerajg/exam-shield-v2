import platform
import subprocess
import os
import ctypes
import winreg
import string

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

    # ── USB / Pendrive Management ────────────────────────────────────────────

    def eject_usb_drive(self, drive_letter: str) -> tuple:
        """Safely eject a USB drive (e.g. 'E:').  Returns (success, message)."""
        drive_letter = drive_letter.rstrip('\\').rstrip('/').upper()
        if not drive_letter.endswith(':'):
            drive_letter += ':'
        try:
            # Use DeviceIoControl via subprocess shortcut: the 'mountvol' trick
            # For a proper eject we call the Win32 API via ctypes
            GENERIC_READ  = 0x80000000
            GENERIC_WRITE = 0x40000000
            OPEN_EXISTING = 3
            FILE_SHARE_READ  = 0x00000001
            FILE_SHARE_WRITE = 0x00000002
            IOCTL_STORAGE_EJECT_MEDIA = 0x2D4808

            handle = ctypes.windll.kernel32.CreateFileW(
                f'\\\\.\\{drive_letter}',
                GENERIC_READ | GENERIC_WRITE,
                FILE_SHARE_READ | FILE_SHARE_WRITE,
                None, OPEN_EXISTING, 0, None
            )
            INVALID_HANDLE = ctypes.c_void_p(-1).value
            if handle == INVALID_HANDLE:
                err = ctypes.windll.kernel32.GetLastError()
                return (False, f'Cannot open drive handle (error {err}). Drive may already be ejected.')

            bytes_returned = ctypes.c_ulong(0)
            result = ctypes.windll.kernel32.DeviceIoControl(
                handle, IOCTL_STORAGE_EJECT_MEDIA,
                None, 0, None, 0,
                ctypes.byref(bytes_returned), None
            )
            ctypes.windll.kernel32.CloseHandle(handle)

            if result:
                self.logger.log_activity('USB_EJECTED', f'Drive {drive_letter} safely ejected')
                return (True, f'Drive {drive_letter} safely ejected.')
            else:
                err = ctypes.windll.kernel32.GetLastError()
                return (False, f'Eject failed (error {err}). Close any files on the drive first.')
        except Exception as e:
            return (False, f'Eject error: {e}')

    def disable_usb_storage_registry(self) -> bool:
        """Block ALL USB mass-storage devices by setting USBSTOR Start=4 in the registry.
        Requires Administrator.  Takes effect for newly inserted drives (existing
        connections are not disconnected — use eject_usb_drive for that)."""
        try:
            key_path = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path,
                                 0, winreg.KEY_SET_VALUE | winreg.KEY_WOW64_64KEY)
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)  # 4 = disabled
            winreg.CloseKey(key)
            self.logger.log_activity('USB_BLOCKED', 'USB storage disabled via registry (USBSTOR Start=4)')
            return True
        except PermissionError:
            self.logger.log_activity('USB_BLOCK_ERROR', 'Permission denied — run as Administrator to block USB storage')
            return False
        except Exception as e:
            self.logger.log_activity('USB_BLOCK_ERROR', f'Failed to disable USB storage: {e}')
            return False

    def enable_usb_storage_registry(self) -> bool:
        """Re-enable USB mass-storage devices (USBSTOR Start=3)."""
        try:
            key_path = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path,
                                 0, winreg.KEY_SET_VALUE | winreg.KEY_WOW64_64KEY)
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 3)  # 3 = manual / enabled
            winreg.CloseKey(key)
            self.logger.log_activity('USB_UNBLOCKED', 'USB storage re-enabled via registry (USBSTOR Start=3)')
            return True
        except PermissionError:
            self.logger.log_activity('USB_ERROR', 'Permission denied — cannot restore USB storage')
            return False
        except Exception as e:
            self.logger.log_activity('USB_ERROR', f'Failed to enable USB storage: {e}')
            return False

    def get_usbstor_status(self) -> str:
        """Return 'blocked', 'enabled', or 'unknown'."""
        try:
            key_path = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path,
                                 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
            value, _ = winreg.QueryValueEx(key, 'Start')
            winreg.CloseKey(key)
            return 'blocked' if value == 4 else 'enabled'
        except Exception:
            return 'unknown'

    def get_usb_drive_info(self) -> list:
        """Return a list of dicts with info about each connected USB drive."""
        drives = self.get_connected_usb_drives()
        info = []
        for drive in drives:
            root = drive if drive.endswith('\\') else drive + '\\'
            d = {'letter': drive, 'label': 'Unknown', 'total': 0, 'free': 0}
            try:
                vol_name = ctypes.create_unicode_buffer(261)
                ctypes.windll.kernel32.GetVolumeInformationW(
                    root, vol_name, 261, None, None, None, None, 0)
                d['label'] = vol_name.value or 'Unlabeled'
            except Exception:
                pass
            try:
                free_bytes   = ctypes.c_ulonglong(0)
                total_bytes  = ctypes.c_ulonglong(0)
                ctypes.windll.kernel32.GetDiskFreeSpaceExW(
                    root, None, ctypes.byref(total_bytes), ctypes.byref(free_bytes))
                d['total'] = total_bytes.value
                d['free']  = free_bytes.value
            except Exception:
                pass
            info.append(d)
        return info
