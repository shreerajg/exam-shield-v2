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
        self.root.title("Exam Shield Premium - System Restoration Tool")
        self.root.geometry("520x450")
        self.root.resizable(False, False)
        
        # Premium color scheme 
        self.colors = {
            'primary': '#1e3d59',      
            'secondary': '#17223b',     
            'accent': '#ffc947',       
            'success': '#27ae60',      
            'danger': '#e74c3c',       
            'surface': '#f8f9fa',      
            'text_primary': '#2c3e50', 
            'text_secondary': '#7f8c8d', 
            'white': '#ffffff',
            'gradient_start': '#1e3d59',
            'gradient_end': '#2980b9'
        }
        
        self.root.configure(bg=self.colors['surface'])
        self.setup_ui()
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - 260
        y = (self.root.winfo_screenheight() // 2) - 225
        self.root.geometry(f"520x450+{x}+{y}")

    def create_gradient_frame(self, parent, width, height):
        canvas = tk.Canvas(parent, width=width, height=height, highlightthickness=0)
        for i in range(height):
            ratio = i / height
            r1, g1, b1 = int(self.colors['gradient_start'][1:3], 16), int(self.colors['gradient_start'][3:5], 16), int(self.colors['gradient_start'][5:7], 16)
            r2, g2, b2 = int(self.colors['gradient_end'][1:3], 16), int(self.colors['gradient_end'][3:5], 16), int(self.colors['gradient_end'][5:7], 16)
            
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            
            color = f"#{r:02x}{g:02x}{b:02x}"
            canvas.create_line(0, i, width, i, fill=color, width=1)
        return canvas

    def setup_ui(self):
        # Header section with gradient
        header_canvas = self.create_gradient_frame(self.root, 520, 120)
        header_canvas.pack(fill=tk.X)
        
        header_canvas.create_text(260, 40, text="⚠️", font=("Segoe UI", 36), fill=self.colors['accent'])
        header_canvas.create_text(260, 85, text="EMERGENCY RESTORE", font=("Segoe UI", 20, "bold"), fill=self.colors['white'])
        
        # Content Area
        content = tk.Frame(self.root, bg=self.colors['surface'])
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        # Advisory panel
        advisory_frame = tk.Frame(content, bg='#fff8e1', bd=1, relief=tk.FLAT)
        advisory_frame.pack(fill=tk.X, pady=(0, 20))
        
        accent_line = tk.Frame(advisory_frame, bg=self.colors['accent'], height=3)
        accent_line.pack(fill=tk.X)
        
        info_text = (
            "This tool will forcefully repair your system if Exam Shield "
            "interrupted unexpectedly. It unlocks network access, kills "
            "lingering processes, and restores the Windows hosts file."
        )
        tk.Message(advisory_frame, text=info_text, width=420, font=("Segoe UI", 10), 
                   bg='#fff8e1', fg=self.colors['text_primary']).pack(padx=15, pady=15)

        # Status Label
        self.status_var = tk.StringVar(value="Status: Ready to begin restoration.")
        self.status_label = tk.Label(content, textvariable=self.status_var, font=("Segoe UI", 10, "bold"), 
                                     bg=self.colors['surface'], fg=self.colors['secondary'])
        self.status_label.pack(pady=(0, 20))

        # Action Button Container
        btn_container = tk.Frame(content, bg=self.colors['surface'])
        btn_container.pack(fill=tk.X, pady=(10, 0))

        self.restore_btn = tk.Button(btn_container, text="🚀 INITIATE SYSTEM REPAIR", 
                                     font=("Segoe UI", 12, "bold"), bg=self.colors['danger'], fg=self.colors['white'], 
                                     relief=tk.FLAT, bd=0, cursor="hand2", command=self.start_restore, 
                                     padx=20, pady=12, activebackground='#c0392b', activeforeground=self.colors['white'])
        self.restore_btn.pack(fill=tk.X)

    def update_status(self, text, is_error=False, is_success=False):
        self.status_var.set(f"Status: {text}")
        if is_error:
            self.status_label.config(fg=self.colors['danger'])
        elif is_success:
            self.status_label.config(fg=self.colors['success'])
        else:
            self.status_label.config(fg=self.colors['primary'])

    def start_restore(self):
        self.restore_btn.config(state=tk.DISABLED, bg="#95a5a6", text="REPAIR IN PROGRESS...")
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
        self.root.after(0, lambda: self.restore_btn.config(state=tk.NORMAL, bg=self.colors['success'], text="RESTORE COMPLETED"))

if __name__ == "__main__":
    if not is_admin():
        run_as_admin()
        sys.exit(0)
    
    root = tk.Tk()
    app = EmergencyRestoreApp(root)
    root.mainloop()
