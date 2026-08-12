"""
Exam Shield - Main Application Entry Point
Enhanced Version with Advanced Security Features
"""
<<<<<<< HEAD

=======
>>>>>>> 8516873 (Initial commit: Project version 1)
import tkinter as tk
from tkinter import messagebox
import sys
import os
import hashlib
import ctypes
import subprocess
from database_manager import DatabaseManager
from admin_panel import AdminPanel
from security_manager import SecurityManager
from system_tray import SystemTray
import threading

<<<<<<< HEAD
# Import patches to fix missing or broken functionality
import admin_panel_selective_patch
import security_manager_toggles_patch
import mouse_manager_pump_patch
import mouse_manager_hook_diagnostics
import theme

=======
>>>>>>> 8516873 (Initial commit: Project version 1)
class ExamShield:
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
=======
            
        self.root = tk.Tk()
        self.root.title("Exam Shield v1.1 - Admin Login")
        self.root.geometry("450x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#f5f5f5')
>>>>>>> 8516873 (Initial commit: Project version 1)
        
        self.db_manager = DatabaseManager()
        self.security_manager = None
        self.system_tray = None
        
        self.setup_ui()
        self.center_window()

<<<<<<< HEAD
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
        self.root.configure(bg=self.colors['surface'])

    def change_theme(self, event=None):
        self.current_theme = self.theme_var.get()
        self.load_theme(self.current_theme)
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_ui()

=======
>>>>>>> 8516873 (Initial commit: Project version 1)
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

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
<<<<<<< HEAD
            
            sys.exit(0)
=======
                sys.exit(0)
>>>>>>> 8516873 (Initial commit: Project version 1)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to restart with admin privileges: {e}")
            sys.exit(1)

    def center_window(self):
        self.root.update_idletasks()
<<<<<<< HEAD
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
        
        username_label = tk.Label(username_container, text="👤 Username", 
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
        
        password_label = tk.Label(password_container, text="🔑 Password", 
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
        
        # Login button 
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
        
        # Theme selector
        theme_frame = tk.Frame(footer_frame, bg=self.colors['surface'])
        theme_frame.pack(pady=5)
        tk.Label(theme_frame, text="Theme:", bg=self.colors['surface'], fg=self.colors['text_secondary'], font=("Segoe UI", 9)).pack(side=tk.LEFT)
        if not hasattr(self, 'theme_var'):
            self.theme_var = tk.StringVar(value=self.current_theme)
        theme_combo = ttk.Combobox(theme_frame, textvariable=self.theme_var, values=["light", "dark", "pink"], width=10, state="readonly", font=("Segoe UI", 9))
        theme_combo.pack(side=tk.LEFT, padx=5)
        theme_combo.bind("<<ComboboxSelected>>", self.change_theme)
        
        # Event bindings
=======
        x = (self.root.winfo_screenwidth() // 2) - 225
        y = (self.root.winfo_screenheight() // 2) - 300
        self.root.geometry(f"450x600+{x}+{y}")

    def setup_ui(self):
        # Header section
        header_frame = tk.Frame(self.root, bg='#2196F3', height=120)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(header_frame, text="🛡️", font=("Arial", 36), bg='#2196F3', fg='white')
        title_label.pack(pady=(15, 5))
        
        app_title = tk.Label(header_frame, text="EXAM SHIELD", font=("Arial", 18, "bold"), bg='#2196F3', fg='white')
        app_title.pack()
        
        subtitle = tk.Label(header_frame, text="Advanced Secure Exam Environment v1.1 [ADMIN MODE]",
                           font=("Arial", 10), bg='#2196F3', fg='#E3F2FD')
        subtitle.pack(pady=(2, 15))
        
        # Main content area
        content_frame = tk.Frame(self.root, bg='#f5f5f5')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # Login form
        form_frame = tk.Frame(content_frame, bg='white', relief=tk.RAISED, bd=2)
        form_frame.pack(fill=tk.X)
        
        # Form header
        form_header = tk.Label(form_frame, text="Admin Login Required", font=("Arial", 14, "bold"),
                              bg='white', fg='#333', pady=20)
        form_header.pack()
        
        # Username section
        username_frame = tk.Frame(form_frame, bg='white')
        username_frame.pack(fill=tk.X, padx=30, pady=(0, 15))
        
        tk.Label(username_frame, text="Username", font=("Arial", 11), bg='white', fg='#666').pack(anchor=tk.W, pady=(0, 5))
        
        self.username_var = tk.StringVar(value="admin")
        username_entry = tk.Entry(username_frame, textvariable=self.username_var,
                                 font=("Arial", 12), width=30, relief=tk.SOLID, bd=1,
                                 highlightthickness=2, highlightcolor='#2196F3')
        username_entry.pack(fill=tk.X, ipady=8)
        
        # Password section
        password_frame = tk.Frame(form_frame, bg='white')
        password_frame.pack(fill=tk.X, padx=30, pady=(0, 25))
        
        tk.Label(password_frame, text="Password", font=("Arial", 11), bg='white', fg='#666').pack(anchor=tk.W, pady=(0, 5))
        
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(password_frame, textvariable=self.password_var,
                                 font=("Arial", 12), width=30, show="*", relief=tk.SOLID, bd=1,
                                 highlightthickness=2, highlightcolor='#2196F3')
        password_entry.pack(fill=tk.X, ipady=8)
        
        # Buttons section
        button_frame = tk.Frame(form_frame, bg='white')
        button_frame.pack(fill=tk.X, padx=30, pady=(0, 30))
        
        login_btn = tk.Button(button_frame, text="🔐 LOGIN", command=self.login,
                             bg='#4CAF50', fg='white', font=("Arial", 12, "bold"),
                             relief=tk.FLAT, cursor='hand2', width=15, pady=10)
        login_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        cancel_btn = tk.Button(button_frame, text="❌ EXIT", command=self.exit_app,
                              bg='#F44336', fg='white', font=("Arial", 12, "bold"),
                              relief=tk.FLAT, cursor='hand2', width=15, pady=10)
        cancel_btn.pack(side=tk.RIGHT)
        
        # Info section
        info_frame = tk.Frame(content_frame, bg='#f5f5f5')
        info_frame.pack(fill=tk.X, pady=(20, 0))
        
        if not self.db_manager.admin_exists():
            info_box = tk.Frame(info_frame, bg='#E8F5E8', relief=tk.SOLID, bd=1)
            info_box.pack(fill=tk.X, pady=10)
            
            info_text = tk.Label(info_box, text="ℹ️ First Time Setup\nDefault: admin / admin",
                                font=("Arial", 10), bg='#E8F5E8', fg='#2E7D32',
                                justify=tk.CENTER, pady=15)
            info_text.pack()
        
        # Admin privileges confirmed box
        admin_confirmed_box = tk.Frame(info_frame, bg='#C8E6C9', relief=tk.SOLID, bd=1)
        admin_confirmed_box.pack(fill=tk.X, pady=(10, 0))
        
        admin_confirmed_label = tk.Label(admin_confirmed_box,
                                        text="✅ Administrator Privileges Confirmed\nAll security features available",
                                        font=("Arial", 9, "bold"), bg='#C8E6C9', fg='#2E7D32',
                                        justify=tk.CENTER, pady=10)
        admin_confirmed_label.pack()
        
        # Features info box
        features_box = tk.Frame(info_frame, bg='#E3F2FD', relief=tk.SOLID, bd=1)
        features_box.pack(fill=tk.X, pady=(10, 0))
        
        features_title = tk.Label(features_box, text="🔒 Security Features",
                                 font=("Arial", 10, "bold"), bg='#E3F2FD', fg='#1976D2')
        features_title.pack(pady=(10, 5))
        
        features_list = [
            "• Advanced keyboard shortcut blocking",
            "• Mouse button restriction & suppression",
            "• Multi-layer internet/website blocking",
            "• Process monitoring & auto-termination",
            "• Window protection & fullscreen enforcement",
            "• Real-time security event logging"
        ]
        
        for feature in features_list:
            feature_label = tk.Label(features_box, text=feature, font=("Arial", 8),
                                    bg='#E3F2FD', fg='#1976D2', anchor='w')
            feature_label.pack(fill=tk.X, padx=15)
        
        # FIXED: Updated admin shortcut info to Ctrl+Shift+Y
        shortcut_box = tk.Frame(info_frame, bg='#FFF3E0', relief=tk.SOLID, bd=1)
        shortcut_box.pack(fill=tk.X, pady=(10, 0))
        
        shortcut_label = tk.Label(shortcut_box,
                                 text="🔑 Emergency Admin Access: Ctrl+Shift+Y\n"
                                      "Use this shortcut during lockdown to access admin panel",
                                 font=("Arial", 9), bg='#FFF3E0', fg='#F57C00',
                                 justify=tk.CENTER, pady=10)
        shortcut_label.pack()
        
        tk.Label(features_box, text="", bg='#E3F2FD').pack(pady=(0, 10))  # Spacer
        
        # Version info
        version_label = tk.Label(content_frame, 
                                text="Version 1.1 - Enhanced Security Suite [Administrator Mode]",
                                font=("Arial", 8), bg='#f5f5f5', fg='#999')
        version_label.pack(side=tk.BOTTOM, pady=(20, 0))
        
        # Bind events
>>>>>>> 8516873 (Initial commit: Project version 1)
        password_entry.bind("<Return>", lambda e: self.login())
        username_entry.bind("<Return>", lambda e: password_entry.focus())
        self.root.bind("<Escape>", lambda e: self.exit_app())
        
        # Set initial focus
        if self.username_var.get():
            password_entry.focus()
        else:
            username_entry.focus()

<<<<<<< HEAD
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

=======
>>>>>>> 8516873 (Initial commit: Project version 1)
    def login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        if not username:
<<<<<<< HEAD
            messagebox.showerror("Authentication Error", "Please enter username")
            return
        
        if not password:
            messagebox.showerror("Authentication Error", "Please enter password")
=======
            messagebox.showerror("Error", "Please enter username")
            return
        if not password:
            messagebox.showerror("Error", "Please enter password")
>>>>>>> 8516873 (Initial commit: Project version 1)
            return
        
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
<<<<<<< HEAD
            
            if self.db_manager.verify_admin(username, password_hash):
                self.start_admin_session()
            else:
                messagebox.showerror("Authentication Failed", 
                                   "Invalid username or password!\n\nPlease check your credentials and try again.")
                self.password_var.set("")
        except Exception as e:
            messagebox.showerror("Authentication Error", f"Login error: {str(e)}")
=======
            if self.db_manager.verify_admin(username, password_hash):
                self.start_admin_session()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password!")
                self.password_var.set("")
        except Exception as e:
            messagebox.showerror("Error", f"Login error: {str(e)}")
>>>>>>> 8516873 (Initial commit: Project version 1)

    def start_admin_session(self):
        try:
            self.root.withdraw()
            
<<<<<<< HEAD
            # Initialize security manager
            self.security_manager = SecurityManager(self.db_manager)
            
            self.db_manager.log_activity("ADMIN_LOGIN_SUCCESS",
                                       "Administrator authenticated with elevated privileges")
            
            # Create admin panel
            admin_panel = AdminPanel(self.db_manager, self.security_manager, self.root)
            
            # Initialize system tray
=======
            self.security_manager = SecurityManager(self.db_manager)
            
            self.db_manager.log_activity("ADMIN_LOGIN_SUCCESS", 
                                        f"Admin logged in with elevated privileges")
            
            admin_panel = AdminPanel(self.db_manager, self.security_manager, self.root)
            
>>>>>>> 8516873 (Initial commit: Project version 1)
            self.system_tray = SystemTray(admin_panel, self.security_manager)
            tray_thread = threading.Thread(target=self.system_tray.run, daemon=True)
            tray_thread.start()
            
<<<<<<< HEAD
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
=======
            # FIXED: Updated success message to show Ctrl+Shift+Y
            messagebox.showinfo("🔒 Exam Shield Loaded",
                               "Exam Shield loaded successfully!\n\n"
                               "✅ All security modules initialized\n"
                               "✅ Admin panel ready\n"
                               "✅ System tray active\n"
                               "✅ Administrator privileges confirmed\n\n"
                               "🔑 Emergency Admin Access: Ctrl+Shift+Y\n"
                               "Use this during lockdown to access admin panel")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start: {str(e)}")
            self.root.deiconify()

    def exit_app(self):
        if messagebox.askyesno("Exit", "Close Exam Shield?\n\nThis will terminate all security features."):
            try:
                self.db_manager.log_activity("APPLICATION_EXIT", "Exam Shield closed by user")
>>>>>>> 8516873 (Initial commit: Project version 1)
            except:
                pass
            self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    try:
        app = ExamShield()
        if hasattr(app, 'root'):
            app.run()
    except Exception as e:
<<<<<<< HEAD
        messagebox.showerror("Startup Error", 
                           f"Exam Shield Premium failed to start:\n{str(e)}")
=======
        messagebox.showerror("Startup Error", f"Application failed to start:\n{str(e)}")
>>>>>>> 8516873 (Initial commit: Project version 1)
