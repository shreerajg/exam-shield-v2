"""
Exam Shield - Main Application Entry Point
Enhanced Version v2.0 with Advanced Security Features and Theme Support
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os
import hashlib
import ctypes
import subprocess
import threading
import atexit
import traceback

# Ensure project root is on the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.database_manager import DatabaseManager
from src.security_manager import SecurityManager
from src.system_tray import SystemTray
import src.theme as theme


# Lazy import of admin panel (to avoid circular imports)
_AdminPanel = None
def get_admin_panel():
    global _AdminPanel
    if _AdminPanel is None:
        from src.admin_panel import AdminPanel
        _AdminPanel = AdminPanel
    return _AdminPanel


class ExamShield:
    """Main application class for Exam Shield v2.0"""

    def __init__(self):
        if not self.is_admin():
            self.restart_as_admin()
            return

        self.root = tk.Tk()
        self.root.title("Exam Shield Premium v2.0 - Admin Login")
        self.root.geometry("520x720")
        self.root.resizable(False, False)

        self.current_theme = "light"
        self.load_theme(self.current_theme)

        self.db_manager = DatabaseManager()
        self.security_manager = None
        self.system_tray = None

        self.setup_ui()
        self.center_window()
        # Animate window in after centering
        self._anim = theme.AnimationManager(self.root)
        self._anim.fade_in(self.root, duration=350)

    # ── Theme ────────────────────────────────────────────────────────────────

    def load_theme(self, theme_name):
        t = theme.get_theme(theme_name)
        tc = t.colors
        if theme_name == "light":
            self.colors = {
                'primary': '#1e3d59', 'secondary': '#17223b', 'accent': '#ffc947',
                'success': '#27ae60', 'danger': '#e74c3c', 'surface': '#f8f9fa',
                'text_primary': '#2c3e50', 'text_secondary': '#7f8c8d', 'white': '#ffffff',
                'light_blue': '#ecf4ff', 'gradient_start': '#1e3d59', 'gradient_end': '#2980b9'
            }
        else:
            self.colors = {
                'primary': tc['primary'], 'secondary': tc['secondary'], 'accent': tc['warning'],
                'success': tc['success'], 'danger': tc['danger'], 'surface': tc['surface'],
                'text_primary': tc['text_primary'], 'text_secondary': tc['text_secondary'],
                'white': tc['card'], 'light_blue': tc['background'],
                'gradient_start': tc['primary_dark'], 'gradient_end': tc['primary_light']
            }
        if hasattr(self, 'root'):
            self.root.configure(bg=self.colors['surface'])

    def change_theme(self, event=None):
        self.current_theme = self.theme_var.get()
        self.load_theme(self.current_theme)
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_ui()

    # ── UI Setup ─────────────────────────────────────────────────────────────

    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - 260
        y = (self.root.winfo_screenheight() // 2) - 360
        self.root.geometry(f"520x720+{x}+{y}")

    def create_gradient_frame(self, parent, width, height):
        canvas = tk.Canvas(parent, width=width, height=height, highlightthickness=0)
        gs = self.colors['gradient_start']
        ge = self.colors['gradient_end']
        r1, g1, b1 = int(gs[1:3], 16), int(gs[3:5], 16), int(gs[5:7], 16)
        r2, g2, b2 = int(ge[1:3], 16), int(ge[3:5], 16), int(ge[5:7], 16)
        for i in range(height):
            ratio = i / height
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            canvas.create_line(0, i, width, i, fill=f"#{r:02x}{g:02x}{b:02x}", width=1)
        return canvas

    def setup_ui(self):
        # Header gradient
        header_canvas = self.create_gradient_frame(self.root, 520, 180)
        header_canvas.pack(fill=tk.X)

        shield_icon = header_canvas.create_text(260, 55, text="🛡️", font=("Segoe UI", 40), fill=self.colors['accent'])
        header_canvas.create_text(260, 110, text="EXAM SHIELD PREMIUM", font=("Segoe UI", 22, "bold"), fill=self.colors['white'])
        header_canvas.create_text(260, 140, text="v2.0 | Secure Examination System", font=("Segoe UI", 11), fill="#a8c8e8")
        
        # Start Pulse Animation
        anim_manager = theme.AnimationManager(self.root)
        anim_manager.pulse_text_color(header_canvas, shield_icon, self.colors['accent'], '#ffffff', duration=1500)

        # Card container
        card = tk.Frame(self.root, bg=self.colors['surface'])
        card.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        # Title
        tk.Label(card, text="Admin Login", font=("Segoe UI", 16, "bold"),
                 bg=self.colors['surface'], fg=self.colors['primary']).pack(pady=(0, 5))
        tk.Label(card, text="Enter your credentials to access the control panel",
                 font=("Segoe UI", 10), bg=self.colors['surface'],
                 fg=self.colors['text_secondary']).pack(pady=(0, 20))

        # Username
        tk.Label(card, text="👤 Username", font=("Segoe UI", 10, "bold"),
                 bg=self.colors['surface'], fg=self.colors['text_primary']).pack(anchor=tk.W)
        self.username_var = tk.StringVar()
        username_entry = tk.Entry(card, textvariable=self.username_var, font=("Segoe UI", 12),
                                  relief=tk.FLAT, bd=5, bg='white', width=30)
        username_entry.pack(fill=tk.X, pady=(3, 15), ipady=8)
        self._anim.bind_entry_glow(username_entry, normal_color='white', focus_color='#dbeafe')

        # Password
        tk.Label(card, text="🔑 Password", font=("Segoe UI", 10, "bold"),
                 bg=self.colors['surface'], fg=self.colors['text_primary']).pack(anchor=tk.W)
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(card, textvariable=self.password_var, show="*",
                                  font=("Segoe UI", 12), relief=tk.FLAT, bd=5, bg='white', width=30)
        password_entry.pack(fill=tk.X, pady=(3, 20), ipady=8)
        self._anim.bind_entry_glow(password_entry, normal_color='white', focus_color='#dbeafe')

        # Login button
        login_btn = tk.Button(card, text="🔐  LOGIN TO CONTROL CENTER",
                              command=self.attempt_login,
                              bg=self.colors['primary'], fg=self.colors['white'],
                              font=("Segoe UI", 12, "bold"), relief=tk.FLAT,
                              cursor='hand2', padx=20, pady=12,
                              activebackground='#17223b', activeforeground='white')
        login_btn.pack(fill=tk.X, pady=(10, 10))
        # Animated shimmer hover + press feedback on login button
        self._anim.bind_shimmer_hover(login_btn, self.colors['primary'], self.colors.get('gradient_start', '#17223b'))
        login_btn.bind('<ButtonPress-1>', lambda e: self._anim.button_press_effect(login_btn), add='+')

        # Change password button
        cp_btn = tk.Button(card, text="🔄 Change Password",
                  command=self.show_change_password,
                  bg=self.colors['secondary'] if 'secondary' in self.colors else '#17223b',
                  fg=self.colors['white'], font=("Segoe UI", 10), relief=tk.FLAT,
                  cursor='hand2', pady=6)
        cp_btn.pack(fill=tk.X, pady=(0, 15))
        self._anim.bind_shimmer_hover(cp_btn,
                                      self.colors['secondary'] if 'secondary' in self.colors else '#17223b',
                                      '#2c3e50')
        # Store card for shake animation reference
        self._login_card = card

        # Status label
        self.login_status = tk.Label(card, text="", font=("Segoe UI", 10),
                                     bg=self.colors['surface'], fg=self.colors['danger'])
        self.login_status.pack()

        # Separator
        tk.Frame(card, bg=self.colors.get('border', '#dee2e6'), height=1).pack(fill=tk.X, pady=15)

        # Theme selector
        theme_frame = tk.Frame(card, bg=self.colors['surface'])
        theme_frame.pack(fill=tk.X)
        tk.Label(theme_frame, text="Theme:", bg=self.colors['surface'],
                 fg=self.colors['text_secondary'], font=("Segoe UI", 9)).pack(side=tk.LEFT)
        if not hasattr(self, 'theme_var'):
            self.theme_var = tk.StringVar(value=self.current_theme)
        theme_combo = ttk.Combobox(theme_frame, textvariable=self.theme_var,
                                   values=["light", "dark", "pink"],
                                   state="readonly", width=10, font=("Segoe UI", 9))
        theme_combo.pack(side=tk.LEFT, padx=5)
        theme_combo.bind("<<ComboboxSelected>>", self.change_theme)

        # Footer
        footer = tk.Frame(self.root, bg=self.colors['primary'], height=40)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        footer.pack_propagate(False)
        tk.Label(footer, text="Exam Shield Premium © 2024 | Group A73, A74, A77",
                 font=("Segoe UI", 8), bg=self.colors['primary'], fg='#7fa8cc').pack(pady=12)

        # Key bindings
        password_entry.bind("<Return>", lambda e: self.attempt_login())
        username_entry.bind("<Return>", lambda e: password_entry.focus())
        username_entry.focus()

    # ── Auth ─────────────────────────────────────────────────────────────────

    def attempt_login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get()

        if not username or not password:
            self.login_status.config(text="⚠️ Please enter username and password", fg=self.colors['danger'])
            return

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        if self.db_manager.verify_admin(username, password_hash):
            self.login_status.config(text="✅ Login successful! Loading control center...", fg=self.colors['success'])
            self.root.after(800, self.launch_admin_panel)
        else:
            self.login_status.config(text="❌ Invalid credentials. Please try again.", fg=self.colors['danger'])
            self.password_var.set("")
            # Shake the login card to signal failure
            if hasattr(self, '_login_card') and hasattr(self, '_anim'):
                self._anim.shake(self._login_card, intensity=10, cycles=4, duration=300)

    def show_change_password(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Change Password")
        dialog.geometry("400x350")
        dialog.configure(bg=self.colors['surface'])
        dialog.transient(self.root)
        dialog.grab_set()

        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - 200
        y = (dialog.winfo_screenheight() // 2) - 175
        dialog.geometry(f"400x350+{x}+{y}")

        header = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text="🔄 Change Admin Password", font=("Segoe UI", 13, "bold"),
                 bg=self.colors['primary'], fg='white').pack(pady=18)

        content = tk.Frame(dialog, bg=self.colors['surface'])
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        fields = {}
        for label, key, show in [("Username", "user", ""), ("Current Password", "cur", "*"), ("New Password", "new", "*"), ("Confirm New Password", "conf", "*")]:
            tk.Label(content, text=label, font=("Segoe UI", 9, "bold"), bg=self.colors['surface'], fg=self.colors['text_primary']).pack(anchor=tk.W)
            var = tk.StringVar()
            fields[key] = var
            tk.Entry(content, textvariable=var, show=show, font=("Segoe UI", 11), relief=tk.FLAT, bd=3, bg='white').pack(fill=tk.X, pady=(2, 8), ipady=5)

        def do_change():
            user = fields['user'].get().strip()
            cur = fields['cur'].get()
            new = fields['new'].get()
            conf = fields['conf'].get()
            if new != conf:
                messagebox.showerror("Error", "New passwords don't match!", parent=dialog)
                return
            if len(new) < 4:
                messagebox.showerror("Error", "Password must be at least 4 characters!", parent=dialog)
                return
            cur_hash = hashlib.sha256(cur.encode()).hexdigest()
            if not self.db_manager.verify_admin(user, cur_hash):
                messagebox.showerror("Error", "Invalid current credentials!", parent=dialog)
                return
            try:
                import sqlite3
                new_hash = hashlib.sha256(new.encode()).hexdigest()
                with sqlite3.connect(self.db_manager.db_path) as conn:
                    conn.execute("UPDATE users SET password_hash=? WHERE username=?", (new_hash, user))
                    conn.commit()
                messagebox.showinfo("Success", "Password changed successfully!", parent=dialog)
                dialog.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to change password: {e}", parent=dialog)

        tk.Button(content, text="✅ Change Password", command=do_change,
                  bg=self.colors['success'], fg='white', font=("Segoe UI", 10, "bold"),
                  relief=tk.FLAT, pady=8, cursor='hand2').pack(fill=tk.X, pady=(5, 0))

    def launch_admin_panel(self):
        self.root.withdraw()
        try:
            self.security_manager = SecurityManager(self.db_manager)
            AdminPanel = get_admin_panel()
            admin_panel = AdminPanel(self.db_manager, self.security_manager, self.root)

            # Start system tray in background thread
            def run_tray():
                try:
                    tray = SystemTray(admin_panel, self.security_manager)
                    tray.run()
                except Exception as e:
                    print(f"System tray error: {e}")

            tray_thread = threading.Thread(target=run_tray, daemon=True)
            tray_thread.start()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch admin panel: {e}")
            self.root.deiconify()

    # ── Utilities ────────────────────────────────────────────────────────────

    @staticmethod
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    @staticmethod
    def restart_as_admin():
        if sys.platform.startswith('win'):
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )

    def run(self):
        self.root.mainloop()


def main():
    # Ensure data/ directory exists
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(data_dir, exist_ok=True)

    app = ExamShield()
    
    def cleanup():
        if app.security_manager and app.security_manager.is_exam_mode:
            print("🚨 Emergency cleanup: Stopping exam mode...")
            try:
                app.security_manager.stop_exam_mode()
            except Exception as e:
                print(f"Cleanup error: {e}")
            
    def global_excepthook(exc_type, exc_value, exc_traceback):
        print("💥 CRITICAL ERROR OCCURRED!", file=sys.stderr)
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        cleanup()
        
    sys.excepthook = global_excepthook
    atexit.register(cleanup)
    
    app.run()


if __name__ == "__main__":
    main()
