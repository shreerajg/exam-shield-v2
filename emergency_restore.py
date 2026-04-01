import os
import sys
import ctypes
import platform
import subprocess
import shutil
import tkinter as tk
from tkinter import messagebox
import threading
import time

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if sys.platform.startswith('win'):
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

class EmergencyRestoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exam Shield - Emergency Restore")
        self.root.geometry("450x380")
        self.root.resizable(False, False)
        
        # Professional color scheme
        self.bg_color = "#1e1e2f"
        self.card_color = "#2a2a3e"
        self.accent_color = "#f39c12"
        self.danger_color = "#e74c3c"
        self.success_color = "#2ecc71"
        self.text_color = "#ecf0f1"
        
        self.root.configure(bg=self.bg_color)
        self.setup_ui()
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - 225
        y = (self.root.winfo_screenheight() // 2) - 190
        self.root.geometry(f"450x380+{x}+{y}")

    def setup_ui(self):
        # Header banner
        header = tk.Frame(self.root, bg=self.card_color, height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        tk.Label(header, text="⚠️", font=("Segoe UI", 30), bg=self.card_color, fg=self.accent_color).pack(side=tk.LEFT, padx=(20, 10))
        tk.Label(header, text="EMERGENCY RESTORE", font=("Segoe UI", 16, "bold"), bg=self.card_color, fg=self.text_color).pack(side=tk.LEFT, anchor='center', pady=(15, 0))

        # Main Content
        content = tk.Frame(self.root, bg=self.bg_color)
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        info_text = (
            "This tool will forcefully repair your system if Exam Shield "
            "was interrupted or crashed and left your computer in a "
            "restricted state."
        )
        tk.Message(content, text=info_text, width=390, font=("Segoe UI", 10), bg=self.bg_color, fg="#bdc3c7").pack(pady=(0, 20))

        # Status Label
        self.status_var = tk.StringVar(value="Status: Ready.")
        self.status_label = tk.Label(content, textvariable=self.status_var, font=("Segoe UI", 10), bg=self.bg_color, fg=self.accent_color)
        self.status_label.pack(pady=(0, 20))

        # Action Button 
        self.restore_btn = tk.Button(content, text="🚀 RESTORE SYSTEM NOW", font=("Segoe UI", 11, "bold"), 
                                     bg=self.danger_color, fg="white", relief=tk.FLAT, bd=0, 
                                     cursor="hand2", command=self.start_restore, padx=20, pady=10)
        self.restore_btn.pack(fill=tk.X)

        # Hover effects
        self.restore_btn.bind("<Enter>", lambda e: self.restore_btn.config(bg="#c0392b"))
        self.restore_btn.bind("<Leave>", lambda e: self.restore_btn.config(bg=self.danger_color))

    def update_status(self, text, is_error=False, is_success=False):
        self.status_var.set(f"Status: {text}")
        if is_error:
            self.status_label.config(fg=self.danger_color)
        elif is_success:
            self.status_label.config(fg=self.success_color)
        else:
            self.status_label.config(fg=self.accent_color)

    def start_restore(self):
        self.restore_btn.config(state=tk.DISABLED, bg="#95a5a6", text="RESTORING...")
        threading.Thread(target=self.run_repair_sequence, daemon=True).start()

    def run_repair_sequence(self):
        self.update_status("Killing lingering Exam Shield processes...")
        try:
            if platform.system().lower() == "windows":
                subprocess.run(['taskkill', '/F', '/IM', 'exam_shield.exe'], capture_output=True)
                subprocess.run(['taskkill', '/F', '/IM', 'python.exe'], capture_output=True)
        except:
            pass
        time.sleep(1)

        self.update_status("Restoring Windows Hosts File (Internet Blocking)...")
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        backup_path = hosts_path + ".exam_shield_backup"
        try:
            if os.path.exists(backup_path):
                shutil.copy2(backup_path, hosts_path)
                os.remove(backup_path)
            elif os.path.exists(hosts_path):
                with open(hosts_path, 'r') as f:
                    content = f.read()
                if "# EXAM SHIELD BLOCKING" in content:
                    start = content.find("# EXAM SHIELD BLOCKING - DO NOT EDIT")
                    end = content.find("# END EXAM SHIELD BLOCKING")
                    if start != -1 and end != -1:
                        end += len("# END EXAM SHIELD BLOCKING")
                        with open(hosts_path, 'w') as f:
                            f.write(content[:start] + content[end:])
        except Exception as e:
            pass
        time.sleep(1)

        self.update_status("Flushing DNS and restoring DHCP...")
        try:
            if platform.system().lower() == "windows":
                for adapt in ['Local Area Connection', 'Wi-Fi', 'Ethernet']:
                    subprocess.run(['netsh', 'interface', 'ip', 'set', 'dns', f'name="{adapt}"', 'source=dhcp'], capture_output=True)
                subprocess.run(['ipconfig', '/flushdns'], capture_output=True)
        except:
            pass
        time.sleep(1)

        self.update_status("System restored successfully!", is_success=True)
        messagebox.showinfo("Success", "System repair completed successfully. Internet and OS functions should now be unlocked.")
        self.root.after(0, lambda: self.restore_btn.config(state=tk.NORMAL, bg=self.success_color, text="RESTORE COMPLETED"))

if __name__ == "__main__":
    if not is_admin():
        run_as_admin()
        sys.exit(0)
    
    root = tk.Tk()
    app = EmergencyRestoreApp(root)
    root.mainloop()
