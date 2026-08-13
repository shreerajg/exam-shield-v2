"""
Security Manager for Exam Shield - FINALIZE TOGGLES IN CLASS
This update adds toggle_* methods directly into the SecurityManager class
"""
import keyboard
import threading
import time
import psutil
from config import Config
from mouse_manager import MouseManager
from network_manager import NetworkManager
from window_manager import WindowManager
from system_integrity import SystemIntegrityManager

class SecurityManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.is_exam_mode = False
        self.blocked_keys = Config.BLOCKED_KEYS.copy()
        self.monitoring_thread = None
        self.hooks_active = False
        self.selective_blocking = Config.SELECTIVE_BLOCKING.copy()
        self.mouse_manager = MouseManager(logger=db_manager)
        self.network_manager = NetworkManager(db_manager)
        self.window_manager = WindowManager(logger=db_manager)
        self.integrity_manager = SystemIntegrityManager(logger=db_manager)
        self.admin_panel = None
        print("✅ Security Manager initialized with all components")
    
    def set_admin_panel(self, admin_panel):
        self.admin_panel = admin_panel
    
    def toggle_mouse_blocking(self, enable: bool):
        try:
            return bool(self.mouse_manager.start_blocking() if enable else self.mouse_manager.stop_blocking())
        except Exception as e:
            print(f"Mouse toggle error: {e}"); return False
    
    def toggle_window_protection(self, enable: bool):
        try:
            return bool(self.window_manager.start_window_protection() if enable else self.window_manager.stop_window_protection())
        except Exception as e:
            print(f"Window toggle error: {e}"); return False
    
    def toggle_internet_blocking(self, enable: bool):
        try:
            if enable:
                self.network_manager.start_blocking(); return True
            else:
                self.network_manager.stop_blocking(); return True
        except Exception as e:
            print(f"Network toggle error: {e}"); return False

    def start_exam_mode(self, selective_options=None):
        if self.is_exam_mode:
            return
        self.is_exam_mode = True
        if selective_options:
            self.selective_blocking.update(selective_options)
        print(f"🔒 Starting selective exam mode with options: {selective_options}")
        if self.selective_blocking.get('keyboard', True):
            print("🔤 Activating keyboard blocking..."); self.setup_keyboard_hooks()
        if self.selective_blocking.get('processes', True):
            print("🔍 Activating process monitoring..."); self.start_process_monitoring()
        if self.selective_blocking.get('mouse', True):
            print("🖱️ Activating mouse blocking..."); print("✅ Mouse blocking activated" if self.mouse_manager.start_blocking() else "❌ Mouse blocking failed")
        if self.selective_blocking.get('internet', True) and Config.BLOCK_INTERNET:
            print("🌐 Activating internet blocking..."); self.network_manager.start_blocking()
        if self.selective_blocking.get('windows', True):
            print("🪟 Activating window protection...")
            try:
                print("✅ Window protection activated" if self.window_manager.start_window_protection() else "❌ Window protection failed")
            except Exception as e:
                print(f"❌ Window protection error: {e}")
                
        # Integrity checks (VM Detection and initial clipboard wipe)
        try:
            is_vm, vm_reason = self.integrity_manager.is_running_in_vm()
            if is_vm:
                print(f"⚠️ SECURITY WARNING: Runtime environment appears to be a Virtual Machine ({vm_reason})")
                self.db_manager.log_activity("INTEGRITY_ALERT", f"Virtual Machine detected: {vm_reason}")
            self.integrity_manager.clear_clipboard()
            print("📋 System clipboard wiped for security")
        except Exception as e:
            print(f"❌ Integrity check error: {e}")

        active_blocks = [k for k, v in self.selective_blocking.items() if v]
        self.db_manager.log_activity("EXAM_MODE_START", f"Selective restrictions: {', '.join(active_blocks)}")
        print(f"🔒 Selective exam mode activated - Active: {', '.join(active_blocks)}")

    def stop_exam_mode(self):
        if not self.is_exam_mode:
            return
        print("🔓 Stopping exam mode - Deactivating all components...")
        self.is_exam_mode = False
        try: self.remove_keyboard_hooks()
        except Exception as e: print(f"Error stopping keyboard hooks: {e}")
        try: self.stop_process_monitoring()
        except Exception as e: print(f"Error stopping process monitoring: {e}")
        try: self.mouse_manager.stop_blocking()
        except Exception as e: print(f"Error stopping mouse blocking: {e}")
        try: self.network_manager.stop_blocking()
        except Exception as e: print(f"Error stopping network blocking: {e}")
        try: self.window_manager.stop_window_protection()
        except Exception as e: print(f"Error stopping window protection: {e}")
        self.db_manager.log_activity("EXAM_MODE_STOP", "All security restrictions deactivated")
        print("🔓 Full exam mode deactivated - All restrictions removed")

    def setup_keyboard_hooks(self):
        try:
            for key_combo in self.blocked_keys:
                keyboard.add_hotkey(key_combo, self.block_key_action, args=(key_combo,), suppress=True)
            keyboard.add_hotkey(Config.ADMIN_ACCESS_KEY, self.admin_access_requested, suppress=False)
            self.hooks_active = True; print("✅ Keyboard hooks activated")
        except Exception as e:
            print(f"❌ Error setting up keyboard hooks: {e}"); self.hooks_active = False

    def remove_keyboard_hooks(self):
        try:
            keyboard.unhook_all(); self.hooks_active = False; print("✅ Keyboard hooks removed")
        except Exception as e:
            print(f"❌ Error removing keyboard hooks: {e}")

    def block_key_action(self, key_combo):
        if self.is_exam_mode:
            self.db_manager.log_activity("BLOCKED_KEY_ATTEMPT", f"Attempted to use: {key_combo}", blocked=True)
            print(f"🚫 Blocked key combination: {key_combo}")

    def admin_access_requested(self):
        print("🔑 Admin access requested via hotkey"); self.db_manager.log_activity("ADMIN_ACCESS_REQUEST", "Admin hotkey pressed")
        if self.admin_panel:
            try: self.admin_panel.show(); print("✅ Admin panel shown")
            except Exception as e: print(f"❌ Error showing admin panel: {e}")

    def start_process_monitoring(self):
        if self.monitoring_thread and self.monitoring_thread.is_alive(): return
        self.monitoring_thread = threading.Thread(target=self._monitor_processes, daemon=True); self.monitoring_thread.start(); print("✅ Process monitoring started")

    def stop_process_monitoring(self):
        if self.monitoring_thread: self.monitoring_thread = None; print("✅ Process monitoring stopped")

    def _monitor_processes(self):
        suspicious_processes = ['taskmgr.exe', 'cmd.exe', 'powershell.exe', 'regedit.exe', 'msconfig.exe', 'discord.exe', 'obs64.exe', 'teamviewer.exe', 'anydesk.exe', 'cheatengine-x86_64.exe']
        print("🔍 Process monitoring active")
        while self.is_exam_mode and self.monitoring_thread:
            try:
                for process in psutil.process_iter(['pid', 'name']):
                    try:
                        if process.info['name'].lower() in suspicious_processes:
                            self.db_manager.log_activity("SUSPICIOUS_PROCESS", f"Detected: {process.info['name']}", blocked=True)
                            try: process.terminate(); print(f"🚫 Terminated suspicious process: {process.info['name']}")
                            except: pass
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue
                        
                # Continuous clipboard clearing while in exam mode
                self.integrity_manager.clear_clipboard()
                
                if self.integrity_manager.is_debugger_present():
                    self.db_manager.log_activity("DEBUGGER_DETECTED", "Debugger presence detected", blocked=True)
                    print("⚠️ DEBUGGER DETECTED! Security risk.")
                
                time.sleep(2)
            except Exception as e:
                print(f"Process monitoring error: {e}"); time.sleep(5)

    def add_blocked_key(self, key_combo):
        if key_combo not in self.blocked_keys:
            self.blocked_keys.append(key_combo)
            if self.hooks_active:
                try: keyboard.add_hotkey(key_combo, self.block_key_action, args=(key_combo,), suppress=True); print(f"✅ Added blocked key: {key_combo}")
                except Exception as e: print(f"❌ Error adding key {key_combo}: {e}")

    def remove_blocked_key(self, key_combo):
        if key_combo in self.blocked_keys:
            self.blocked_keys.remove(key_combo); print(f"✅ Removed blocked key: {key_combo}")

    def get_system_info(self):
        try:
            info = {
                'cpu_percent': psutil.cpu_percent(interval=0.1),
                'memory_percent': psutil.virtual_memory().percent,
                'active_processes': len(psutil.pids()),
                'exam_mode': self.is_exam_mode,
                'hooks_active': self.hooks_active,
                'mouse_blocking': self.mouse_manager.is_active if self.mouse_manager else False,
                'internet_blocked': self.network_manager.is_blocked if self.network_manager else False,
                'window_protection': self.window_manager.is_active if self.window_manager else False
            }; return info
        except Exception as e:
            print(f"Error getting system info: {e}")
            return {'cpu_percent':0,'memory_percent':0,'active_processes':0,'exam_mode':self.is_exam_mode,'hooks_active':self.hooks_active,'mouse_blocking':False,'internet_blocked':False,'window_protection':False}
