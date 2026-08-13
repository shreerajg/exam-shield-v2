"""
Exam Shield - Main Application Entry Point
<<<<<<< HEAD
Enhanced Version v2.0 with Advanced Security Features and Theme Support
=======
Premium Design Version with Enhanced UI/UX
>>>>>>> 1543317 (adding elements in main page)
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os
import hashlib
import ctypes
import subprocess
import threading

<<<<<<< HEAD
# Ensure project root is on the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.database_manager import DatabaseManager
from src.security_manager import SecurityManager
from src.system_tray import SystemTray
import theme

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

=======
class ExamShield:
>>>>>>> 1543317 (adding elements in main page)
    def __init__(self):
        if not self.is_admin():
            self.restart_as_admin()
            return
<<<<<<< HEAD

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

        header_canvas.create_text(260, 55, text="🛡️", font=("Segoe UI", 40), fill=self.colors['accent'])
        header_canvas.create_text(260, 110, text="EXAM SHIELD PREMIUM", font=("Segoe UI", 22, "bold"), fill=self.colors['white'])
        header_canvas.create_text(260, 140, text="v2.0 | Secure Examination System", font=("Segoe UI", 11), fill="#a8c8e8")

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

        # Password
        tk.Label(card, text="🔑 Password", font=("Segoe UI", 10, "bold"),
                 bg=self.colors['surface'], fg=self.colors['text_primary']).pack(anchor=tk.W)
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(card, textvariable=self.password_var, show="*",
                                  font=("Segoe UI", 12), relief=tk.FLAT, bd=5, bg='white', width=30)
        password_entry.pack(fill=tk.X, pady=(3, 20), ipady=8)

        # Login button
        login_btn = tk.Button(card, text="🔐  LOGIN TO CONTROL CENTER",
                              command=self.attempt_login,
                              bg=self.colors['primary'], fg=self.colors['white'],
                              font=("Segoe UI", 12, "bold"), relief=tk.FLAT,
                              cursor='hand2', padx=20, pady=12,
                              activebackground='#17223b', activeforeground='white')
        login_btn.pack(fill=tk.X, pady=(0, 10))

        # Change password button
        tk.Button(card, text="🔄 Change Password",
                  command=self.show_change_password,
                  bg=self.colors['secondary'] if 'secondary' in self.colors else '#17223b',
                  fg=self.colors['white'], font=("Segoe UI", 10), relief=tk.FLAT,
                  cursor='hand2', pady=6).pack(fill=tk.X, pady=(0, 15))

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
=======
        
        self.root = tk.Tk()
        self.root.title("Exam Shield v2.0 - Premium Edition")
        self.root.geometry("520x720")
        self.root.resizable(False, False)
        
        # Premium color scheme
        self.colors = {
            'primary': '#1e3d59',      # Deep navy blue
            'secondary': '#17223b',     # Darker navy
            'accent': '#ffc947',       # Premium gold
            'success': '#27ae60',      # Professional green
            'danger': '#e74c3c',       # Professional red
            'surface': '#f8f9fa',      # Light surface
            'text_primary': '#2c3e50', # Dark text
            'text_secondary': '#7f8c8d', # Gray text
            'white': '#ffffff',
            'light_blue': '#ecf4ff',
            'gradient_start': '#1e3d59',
            'gradient_end': '#2980b9'
        }
        
        self.root.configure(bg=self.colors['surface'])
        
        self.db_manager = DatabaseManager()
        self.security_manager = None
        self.system_tray = None
        
        self.setup_ui()
        self.center_window()

    def is_admin(self):
>>>>>>> 1543317 (adding elements in main page)
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

<<<<<<< HEAD
    @staticmethod
    def restart_as_admin():
        if sys.platform.startswith('win'):
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
=======
    def restart_as_admin(self):
        try:
            result = messagebox.askyesno(
                "Administrator Privileges Required",
                "Exam Shield requires administrator privileges to function properly.\n\n"
                "This is needed for:\n"
                "• Network adapter control\n"
                "• Process monitoring & termination\n"
                "• System-level keyboard/mouse hooks\n"
                "• Firewall rule management\n\n"
                "Click 'Yes' to restart with admin privileges, or 'No' to exit."
            )
            
            if result:
                if getattr(sys, 'frozen', False):
                    script_path = sys.executable
                else:
                    script_path = os.path.abspath(__file__)
                
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas",
                    sys.executable if not getattr(sys, 'frozen', False) else script_path,
                    f'"{script_path}"' if not getattr(sys, 'frozen', False) else "",
                    None, 1
                )
            
            sys.exit(0)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to restart with admin privileges: {e}")
            sys.exit(1)

    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - 260
        y = (self.root.winfo_screenheight() // 2) - 360
        self.root.geometry(f"520x720+{x}+{y}")

    def create_gradient_frame(self, parent, width, height):
        """Create a frame with gradient background effect"""
        canvas = tk.Canvas(parent, width=width, height=height, highlightthickness=0)
        
        # Create gradient effect using multiple rectangles
        for i in range(height):
            # Calculate color interpolation
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
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['surface'])
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Header section with gradient
        header_canvas = self.create_gradient_frame(main_container, 520, 160)
        header_canvas.pack(fill=tk.X)
        
        # Logo and title on gradient background
        header_canvas.create_text(260, 40, text="🛡️", font=("Segoe UI", 42), fill=self.colors['white'])
        header_canvas.create_text(260, 85, text="EXAM SHIELD", font=("Segoe UI", 22, "bold"), fill=self.colors['white'])
        header_canvas.create_text(260, 110, text="Premium Secure Exam Environment v2.0", 
                                font=("Segoe UI", 11), fill=self.colors['light_blue'])
        header_canvas.create_text(260, 135, text="ADMINISTRATOR MODE", 
                                font=("Segoe UI", 9, "bold"), fill=self.colors['accent'])
        
        # Content area
        content_frame = tk.Frame(main_container, bg=self.colors['surface'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)
        
        # Login card with shadow effect
        card_container = tk.Frame(content_frame, bg=self.colors['surface'])
        card_container.pack(fill=tk.X)
        
        # Shadow frame
        shadow_frame = tk.Frame(card_container, bg='#d0d3d4', height=2)
        shadow_frame.pack(fill=tk.X, pady=(2, 0))
        
        # Main login card
        login_card = tk.Frame(card_container, bg=self.colors['white'], relief=tk.FLAT, bd=0)
        login_card.pack(fill=tk.X, pady=(0, 2))
        
        # Add subtle inner border
        border_frame = tk.Frame(login_card, bg='#e9ecef', height=1)
        border_frame.pack(fill=tk.X)
        
        # Card header
        card_header = tk.Frame(login_card, bg=self.colors['white'], height=60)
        card_header.pack(fill=tk.X, pady=(25, 15))
        card_header.pack_propagate(False)
        
        header_icon = tk.Label(card_header, text="🔐", font=("Segoe UI", 20), 
                              bg=self.colors['white'], fg=self.colors['primary'])
        header_icon.pack(side=tk.LEFT, padx=(30, 10))
        
        header_text = tk.Label(card_header, text="Administrator Authentication", 
                              font=("Segoe UI", 16, "bold"), bg=self.colors['white'], 
                              fg=self.colors['text_primary'])
        header_text.pack(side=tk.LEFT, anchor=tk.W)
        
        # Form section
        form_section = tk.Frame(login_card, bg=self.colors['white'])
        form_section.pack(fill=tk.X, padx=30, pady=(0, 30))
        
        # Username field
        username_container = tk.Frame(form_section, bg=self.colors['white'])
        username_container.pack(fill=tk.X, pady=(0, 20))
        
        username_label = tk.Label(username_container, text="Username", 
                                font=("Segoe UI", 11, "bold"), bg=self.colors['white'], 
                                fg=self.colors['text_secondary'])
        username_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.username_var = tk.StringVar(value="admin")
        username_entry = tk.Entry(username_container, textvariable=self.username_var,
                                font=("Segoe UI", 12), relief=tk.FLAT, bd=5,
                                bg='#f8f9fa', fg=self.colors['text_primary'],
                                highlightthickness=2, highlightcolor=self.colors['primary'],
                                insertbackground=self.colors['primary'])
        username_entry.pack(fill=tk.X, ipady=12)
        
        # Password field
        password_container = tk.Frame(form_section, bg=self.colors['white'])
        password_container.pack(fill=tk.X, pady=(0, 25))
        
        password_label = tk.Label(password_container, text="Password", 
                                font=("Segoe UI", 11, "bold"), bg=self.colors['white'], 
                                fg=self.colors['text_secondary'])
        password_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(password_container, textvariable=self.password_var,
                                font=("Segoe UI", 12), show="*", relief=tk.FLAT, bd=5,
                                bg='#f8f9fa', fg=self.colors['text_primary'],
                                highlightthickness=2, highlightcolor=self.colors['primary'],
                                insertbackground=self.colors['primary'])
        password_entry.pack(fill=tk.X, ipady=12)
        
        # Buttons section
        button_container = tk.Frame(form_section, bg=self.colors['white'])
        button_container.pack(fill=tk.X, pady=(10, 0))
        
        # Login button with premium styling
        login_btn = tk.Button(button_container, text="🚀 AUTHENTICATE", command=self.login,
                            bg=self.colors['primary'], fg=self.colors['white'], 
                            font=("Segoe UI", 12, "bold"), relief=tk.FLAT, cursor='hand2', 
                            padx=20, pady=12, activebackground=self.colors['secondary'],
                            activeforeground=self.colors['white'])
        login_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        # Exit button
        exit_btn = tk.Button(button_container, text="❌ EXIT", command=self.exit_app,
                           bg=self.colors['danger'], fg=self.colors['white'], 
                           font=("Segoe UI", 12, "bold"), relief=tk.FLAT, cursor='hand2',
                           padx=20, pady=12, activebackground='#c0392b',
                           activeforeground=self.colors['white'])
        exit_btn.pack(side=tk.RIGHT)
        
        # Information panels
        info_section = tk.Frame(content_frame, bg=self.colors['surface'])
        info_section.pack(fill=tk.X, pady=(25, 0))
        
        # First time setup info (if needed)
        if not self.db_manager.admin_exists():
            setup_panel = self.create_info_panel(info_section, 
                                               "💡 First Time Setup", 
                                               "Default credentials: admin / admin",
                                               self.colors['success'], '#d5e7d8')
            setup_panel.pack(fill=tk.X, pady=(0, 12))
        
        # Admin privileges confirmation
        admin_panel = self.create_info_panel(info_section,
                                           "✅ Administrator Privileges Active",
                                           "All security features are available and operational",
                                           self.colors['success'], '#d5e7d8')
        admin_panel.pack(fill=tk.X, pady=(0, 12))
        
        # Security features panel
        features_panel = self.create_feature_panel(info_section)
        features_panel.pack(fill=tk.X, pady=(0, 12))
        
        # Emergency access info
        emergency_panel = self.create_info_panel(info_section,
                                               "🔑 Emergency Admin Access",
                                               "Use Ctrl+Shift+Y during lockdown to access admin panel",
                                               self.colors['accent'], '#fff8e1')
        emergency_panel.pack(fill=tk.X, pady=(0, 15))
        
        # Footer
        footer_frame = tk.Frame(content_frame, bg=self.colors['surface'])
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        version_label = tk.Label(footer_frame, 
                               text="Exam Shield v2.0 Premium Edition | Enhanced Security Suite",
                               font=("Segoe UI", 9), bg=self.colors['surface'], 
                               fg=self.colors['text_secondary'])
        version_label.pack(pady=10)
        
        # Event bindings
        password_entry.bind("<Return>", lambda e: self.login())
        username_entry.bind("<Return>", lambda e: password_entry.focus())
        self.root.bind("<Escape>", lambda e: self.exit_app())
        
        # Set initial focus
        if self.username_var.get():
            password_entry.focus()
        else:
            username_entry.focus()

    def create_info_panel(self, parent, title, content, accent_color, bg_color):
        """Create a styled information panel"""
        panel = tk.Frame(parent, bg=bg_color, relief=tk.FLAT, bd=0)
        
        # Border accent
        accent_line = tk.Frame(panel, bg=accent_color, height=3)
        accent_line.pack(fill=tk.X)
        
        content_area = tk.Frame(panel, bg=bg_color)
        content_area.pack(fill=tk.X, padx=20, pady=15)
        
        title_label = tk.Label(content_area, text=title, font=("Segoe UI", 10, "bold"),
                             bg=bg_color, fg=accent_color)
        title_label.pack(anchor=tk.W)
        
        content_label = tk.Label(content_area, text=content, font=("Segoe UI", 9),
                               bg=bg_color, fg=self.colors['text_primary'])
        content_label.pack(anchor=tk.W, pady=(3, 0))
        
        return panel

    def create_feature_panel(self, parent):
        """Create the security features panel"""
        panel = tk.Frame(parent, bg=self.colors['light_blue'], relief=tk.FLAT, bd=0)
        
        # Header accent
        header_accent = tk.Frame(panel, bg=self.colors['primary'], height=3)
        header_accent.pack(fill=tk.X)
        
        content_area = tk.Frame(panel, bg=self.colors['light_blue'])
        content_area.pack(fill=tk.X, padx=20, pady=15)
        
        # Title
        title_label = tk.Label(content_area, text="🔒 Premium Security Features",
                             font=("Segoe UI", 11, "bold"), bg=self.colors['light_blue'],
                             fg=self.colors['primary'])
        title_label.pack(anchor=tk.W, pady=(0, 8))
        
        # Features grid
        features = [
            "Advanced keyboard shortcut prevention",
            "Intelligent mouse button restrictions",
            "Multi-layer internet access control",
            "Real-time process monitoring & termination",
            "Comprehensive window protection system",
            "Professional security event logging"
        ]
        
        for i, feature in enumerate(features):
            feature_frame = tk.Frame(content_area, bg=self.colors['light_blue'])
            feature_frame.pack(fill=tk.X, pady=1)
            
            bullet = tk.Label(feature_frame, text="▪", font=("Segoe UI", 10, "bold"),
                            bg=self.colors['light_blue'], fg=self.colors['primary'])
            bullet.pack(side=tk.LEFT, padx=(0, 8))
            
            feature_text = tk.Label(feature_frame, text=feature, font=("Segoe UI", 9),
                                  bg=self.colors['light_blue'], fg=self.colors['text_primary'])
            feature_text.pack(side=tk.LEFT, anchor=tk.W)
        
        return panel

    def login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        if not username:
            messagebox.showerror("Authentication Error", "Please enter username")
            return
        
        if not password:
            messagebox.showerror("Authentication Error", "Please enter password")
            return
        
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            
            if self.db_manager.verify_admin(username, password_hash):
                self.start_admin_session()
            else:
                messagebox.showerror("Authentication Failed", 
                                   "Invalid username or password!\n\nPlease check your credentials and try again.")
                self.password_var.set("")
        except Exception as e:
            messagebox.showerror("Authentication Error", f"Login error: {str(e)}")

    def start_admin_session(self):
        try:
            self.root.withdraw()
            
            # Initialize security manager with proper import
            from security_manager import SecurityManager
            self.security_manager = SecurityManager(self.db_manager)
            
            self.db_manager.log_activity("ADMIN_LOGIN_SUCCESS",
                                       "Administrator authenticated with elevated privileges")
            
            # Create admin panel
            admin_panel = AdminPanel(self.db_manager, self.security_manager, self.root)
            
            # Initialize system tray
            self.system_tray = SystemTray(admin_panel, self.security_manager)
            tray_thread = threading.Thread(target=self.system_tray.run, daemon=True)
            tray_thread.start()
            
            # Success notification
            messagebox.showinfo("🛡️ Exam Shield Premium Loaded",
                              "Exam Shield Premium has been loaded successfully!\n\n"
                              "✅ All security modules initialized\n"
                              "✅ Premium admin panel ready\n"
                              "✅ System tray monitoring active\n"
                              "✅ Administrator privileges confirmed\n\n"
                              "🔑 Emergency Access: Ctrl+Shift+Y\n"
                              "Use this shortcut during lockdown to access admin panel")
        except Exception as e:
            messagebox.showerror("Initialization Error", 
                               f"Failed to start Exam Shield Premium: {str(e)}")
            self.root.deiconify()

    def exit_app(self):
        if messagebox.askyesno("Exit Exam Shield", 
                              "Close Exam Shield Premium?\n\n"
                              "This will terminate all security features and monitoring."):
            try:
                self.db_manager.log_activity("APPLICATION_EXIT", 
                                           "Exam Shield Premium closed by administrator")
            except:
                pass
            self.root.quit()
>>>>>>> 1543317 (adding elements in main page)

    def run(self):
        self.root.mainloop()


def main():
    # Ensure data/ directory exists
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(data_dir, exist_ok=True)

    app = ExamShield()
    app.run()


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    try:
        app = ExamShield()
        if hasattr(app, 'root'):
            app.run()
    except Exception as e:
        messagebox.showerror("Startup Error", 
                           f"Exam Shield Premium failed to start:\n{str(e)}")
>>>>>>> 1543317 (adding elements in main page)
