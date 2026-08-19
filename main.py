"""
Exam Shield - Main Application Entry Point
Enhanced Version v2.0 with Advanced Security Features and Theme Support
"""

import tkinter as tk
from tkinter import messagebox, ttk
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
        self.root.geometry("520x780")
        self.root.resizable(False, False)

        self.current_theme = "dark"
        self.load_theme(self.current_theme)

        self.db_manager = DatabaseManager()
        self.security_manager = None
        self.system_tray = None

        # Create animation manager before setup_ui so first-load animations work
        self._anim = theme.AnimationManager(self.root)
        self.setup_ui()
        self.center_window()
        self._anim.fade_in(self.root, duration=350)

    # ── Theme ────────────────────────────────────────────────────────────────

    def load_theme(self, theme_name):
        t = theme.get_theme(theme_name)
        tc = t.colors
        if theme_name == "light":
            self.colors = {
                'primary':        '#1a56db',
                'secondary':      '#7c3aed',
                'accent':         '#f59e0b',
                'success':        '#059669', 'danger': '#dc2626',
                'surface':        '#f8faff',
                'card':           '#ffffff',
                'text_primary':   '#0f172a',
                'text_secondary': '#475569',
                'white':          '#ffffff',
                'light_blue':     '#eef2ff',
                'border':         '#c7d7fe',
                'gradient_start': '#1a56db',
                'gradient_end':   '#7c3aed',
                'neon_glow':      '#3b82f6',
                'entry_bg':       '#eef2ff',
                'entry_focus':    '#dbeafe',
            }
        elif theme_name == "dark":
            self.colors = {
                'primary':        '#6366f1',
                'secondary':      '#8b5cf6',
                'accent':         '#f59e0b',
                'success':        '#10b981', 'danger': '#ef4444',
                'surface':        '#0d1117',
                'card':           '#161b22',
                'text_primary':   '#e6edf3',
                'text_secondary': '#8b949e',
                'white':          '#ffffff',
                'light_blue':     '#1c2330',
                'border':         '#30363d',
                'gradient_start': '#1e1b4b',
                'gradient_end':   '#312e81',
                'neon_glow':      '#6366f1',
                'entry_bg':       '#21262d',
                'entry_focus':    '#30363d',
            }
        else:  # pink
            self.colors = {
                'primary':        '#db2777',
                'secondary':      '#7c3aed',
                'accent':         '#f59e0b',
                'success':        '#059669', 'danger': '#dc2626',
                'surface':        '#fff5f9',
                'card':           '#ffffff',
                'text_primary':   '#500724',
                'text_secondary': '#9d174d',
                'white':          '#ffffff',
                'light_blue':     '#fce7f3',
                'border':         '#fbb6ce',
                'gradient_start': '#db2777',
                'gradient_end':   '#7c3aed',
                'neon_glow':      '#ec4899',
                'entry_bg':       '#fce7f3',
                'entry_focus':    '#fbcfe8',
            }
        if hasattr(self, 'root'):
            self.root.configure(bg=self.colors['surface'])

    def change_theme(self, event=None):
        self.current_theme = self.theme_var.get()
        self.load_theme(self.current_theme)
        for widget in self.root.winfo_children():
            widget.destroy()
        # Re-create animation manager with new root bg
        self._anim = theme.AnimationManager(self.root)
        self.setup_ui()

    # ── UI Setup ─────────────────────────────────────────────────────────────

    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth()  // 2) - 260
        y = (self.root.winfo_screenheight() // 2) - 390
        self.root.geometry(f"520x780+{x}+{y}")

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
        """Build the premium 3D login interface."""
        c = self.colors
        surf = c['surface']
        self.root.configure(bg=surf)

        # ── Hero header: deep-space gradient ──────────────────────────────────
        header_canvas = self.create_gradient_frame(self.root, 520, 210)
        header_canvas.pack(fill=tk.X)

        # Floating particles / dots for depth
        for (px, py, ps) in [(60,30,3),(440,80,2),(100,160,2),(460,40,4),(200,190,2),(380,170,3)]:
            header_canvas.create_oval(px-ps, py-ps, px+ps, py+ps,
                                      fill='#ffffff22', outline='')

        # Shield icon with glow halo
        header_canvas.create_oval(225, 28, 295, 98,
                                  fill='', outline=c['accent'], width=2)
        shield_item = header_canvas.create_text(
            260, 63, text="🛡️", font=("Segoe UI", 38), fill=c['accent'])
        header_canvas.create_text(
            260, 138, text="EXAM SHIELD PREMIUM",
            font=("Segoe UI", 20, "bold"), fill="#ffffff")
        header_canvas.create_text(
            260, 165, text="v2.0  ·  Secure Examination System",
            font=("Segoe UI", 10), fill="#a5b4fc")
        header_canvas.create_text(
            260, 188, text="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            font=("Segoe UI", 7), fill="#4338ca")

        self._anim.pulse_text_color(header_canvas, shield_item, c['accent'], '#ffffff', duration=2200)

        # Gold + neon accent strip
        accent_bar = tk.Canvas(self.root, height=4, highlightthickness=0, bg=surf)
        accent_bar.pack(fill=tk.X)
        for i in range(520):
            t = i / 520
            r1,g1,b1 = 0xf5,0x9e,0x0b
            r2,g2,b2 = 0x63,0x66,0xf1
            accent_bar.create_line(i, 0, i, 4,
                fill=f'#{int(r1+(r2-r1)*t):02x}{int(g1+(g2-g1)*t):02x}{int(b1+(b2-b1)*t):02x}',
                width=1)

        # ── Login form card ───────────────────────────────────────────────────
        card_bg = c['card']
        card = tk.Frame(self.root, bg=card_bg,
                        highlightbackground=c['border'],
                        highlightthickness=1)
        card.pack(fill=tk.BOTH, expand=True, padx=32, pady=18)

        # Card header row
        card_hdr = tk.Frame(card, bg=card_bg)
        card_hdr.pack(fill=tk.X, padx=22, pady=(20, 0))
        tk.Frame(card_hdr, bg=c['primary'], width=5, height=28).pack(side=tk.LEFT)
        hdr_text = tk.Frame(card_hdr, bg=card_bg)
        hdr_text.pack(side=tk.LEFT, padx=10)
        tk.Label(hdr_text, text="Administrator Login",
                 font=("Segoe UI", 17, "bold"),
                 bg=card_bg, fg=c['primary']).pack(anchor=tk.W)
        tk.Label(hdr_text, text="Sign in to access the control center",
                 font=("Segoe UI", 9),
                 bg=card_bg, fg=c['text_secondary']).pack(anchor=tk.W)

        # Separator
        sep_canvas = tk.Canvas(card, height=2, highlightthickness=0, bg=card_bg)
        sep_canvas.pack(fill=tk.X, padx=22, pady=(14, 18))
        for i in range(456):
            t = i/456
            r1,g1,b1 = 0x63,0x66,0xf1
            r2,g2,b2 = 0x8b,0x5c,0xf6
            sep_canvas.create_line(i, 0, i, 2,
                fill=f'#{int(r1+(r2-r1)*t):02x}{int(g1+(g2-g1)*t):02x}{int(b1+(b2-b1)*t):02x}',
                width=1)

        form = tk.Frame(card, bg=card_bg)
        form.pack(fill=tk.BOTH, expand=True, padx=22)

        # ─ Username ─
        tk.Label(form, text="U S E R N A M E", font=("Segoe UI", 8, "bold"),
                 bg=card_bg, fg=c['text_secondary']).pack(anchor=tk.W)
        self.username_var = tk.StringVar()
        username_entry = tk.Entry(
            form, textvariable=self.username_var,
            font=("Segoe UI", 12), relief=tk.FLAT, bd=0,
            bg=c.get('entry_bg', '#eef2f7'), fg=c['text_primary'], width=30,
            insertbackground=c['primary'])
        username_entry.pack(fill=tk.X, pady=(5, 1), ipady=11)
        tk.Frame(form, bg=c['primary'], height=2).pack(fill=tk.X, pady=(0, 18))
        self._anim.bind_entry_glow(username_entry,
                                   c.get('entry_bg', '#eef2f7'),
                                   c.get('entry_focus', '#dbeafe'))

        # ─ Password ─
        tk.Label(form, text="P A S S W O R D", font=("Segoe UI", 8, "bold"),
                 bg=card_bg, fg=c['text_secondary']).pack(anchor=tk.W)
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(
            form, textvariable=self.password_var, show="●",
            font=("Segoe UI", 12), relief=tk.FLAT, bd=0,
            bg=c.get('entry_bg', '#eef2f7'), fg=c['text_primary'], width=30,
            insertbackground=c['primary'])
        password_entry.pack(fill=tk.X, pady=(5, 1), ipady=11)
        tk.Frame(form, bg=c['primary'], height=2).pack(fill=tk.X, pady=(0, 22))
        self._anim.bind_entry_glow(password_entry,
                                   c.get('entry_bg', '#eef2f7'),
                                   c.get('entry_focus', '#dbeafe'))

        # ─ 3D Sign In Button ─
        btn_frame = tk.Frame(form, bg=card_bg)
        btn_frame.pack(fill=tk.X, pady=(0, 6))
        self._login_btn3d = theme.Button3D(
            btn_frame,
            text="SIGN IN",
            icon="🔐",
            command=self.attempt_login,
            base_color=c['primary'],
            text_color='#ffffff',
            width=432, height=46,
            glow=True,
            glow_color=c.get('neon_glow', c['primary']),
        )
        self._login_btn3d.pack(fill=tk.X)

        # ─ Status message ─
        self.login_status = tk.Label(
            form, text="", font=("Segoe UI", 9),
            bg=card_bg, fg=c['danger'], wraplength=400)
        self.login_status.pack(pady=(2, 10))

        # ─ Divider ─
        tk.Frame(form, bg=c['border'], height=1).pack(fill=tk.X, pady=(0, 12))

        # ─ Change Password (ghost 3D button) ─
        ghost_frame = tk.Frame(form, bg=card_bg)
        ghost_frame.pack(fill=tk.X, pady=(0, 14))
        cp_btn3d = theme.Button3D(
            ghost_frame,
            text="Change Password",
            icon="🔄",
            command=self.show_change_password,
            base_color=c.get('entry_bg', '#e2e8f0'),
            text_color=c['text_secondary'],
            width=432, height=38,
            glow=False,
        )
        cp_btn3d.pack(fill=tk.X)

        # ─ Theme selector ─
        theme_row = tk.Frame(form, bg=card_bg)
        theme_row.pack(fill=tk.X)
        tk.Label(theme_row, text="🎨  Theme:", bg=card_bg,
                 fg=c['text_secondary'], font=("Segoe UI", 9)).pack(side=tk.LEFT)
        if not hasattr(self, 'theme_var'):
            self.theme_var = tk.StringVar(value=self.current_theme)
        theme_combo = ttk.Combobox(
            theme_row, textvariable=self.theme_var,
            values=["dark", "light", "pink"],
            state="readonly", width=10, font=("Segoe UI", 9))
        theme_combo.pack(side=tk.LEFT, padx=8)
        theme_combo.bind("<<ComboboxSelected>>", self.change_theme)

        # Store card ref for shake animation
        self._login_card = card

        # ── Footer with gradient ──────────────────────────────────────────────
        footer_canvas = tk.Canvas(self.root, height=40, highlightthickness=0)
        footer_canvas.pack(fill=tk.X, side=tk.BOTTOM)
        gs = c['gradient_start']; ge = c['gradient_end']
        r1,g1,b1 = int(gs[1:3],16), int(gs[3:5],16), int(gs[5:7],16)
        r2,g2,b2 = int(ge[1:3],16), int(ge[3:5],16), int(ge[5:7],16)
        for i in range(520):
            t = i/520
            footer_canvas.create_line(i, 0, i, 40,
                fill=f'#{int(r1+(r2-r1)*t):02x}{int(g1+(g2-g1)*t):02x}{int(b1+(b2-b1)*t):02x}',
                width=1)
        footer_canvas.create_text(
            260, 20,
            text="Exam Shield Premium © 2024  ·  Group A73, A74, A77",
            font=("Segoe UI", 8), fill='#a5b4fc')

        # ── Key bindings ──────────────────────────────────────────────────────
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
