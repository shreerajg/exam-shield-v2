<<<<<<< HEAD
"""
Exam Shield - Main Application Entry Point
Enhanced Version with Advanced Security Features
"""
<<<<<<< HEAD

=======
>>>>>>> 8516873 (Initial commit: Project version 1)
=======
>>>>>>> de2d156 (Initial commit)
import tkinter as tk
from tkinter import messagebox, ttk
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
=======
class ModernExamShield:
>>>>>>> de2d156 (Initial commit)
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
        self.root.title("Exam Shield Pro v2.0")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
<<<<<<< HEAD
        self.root.configure(bg='#f5f5f5')
>>>>>>> 8516873 (Initial commit: Project version 1)
=======
        
        # Modern styling - FIXED COLORS
        self.setup_colors()
        self.setup_fonts()
>>>>>>> de2d156 (Initial commit)
        
        self.db_manager = DatabaseManager()
        self.security_manager = None
        self.system_tray = None
        
        self.setup_modern_ui()
        self.center_window()

<<<<<<< HEAD
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
=======
    def setup_colors(self):
        """Configure color palette with Tkinter-compatible colors"""
        self.colors = {
            'primary': '#2563EB',
            'primary_dark': '#1D4ED8', 
            'primary_light': '#3B82F6',
            'secondary': '#10B981',
            'secondary_dark': '#059669',
            'success': '#10B981',
            'danger': '#EF4444',
            'danger_dark': '#DC2626',
            'warning': '#F59E0B',
            'warning_dark': '#D97706',
            'info': '#3B82F6',
            'white': '#FFFFFF',
            'light_gray': '#F9FAFB',
            'medium_gray': '#E5E7EB',
            'dark_gray': '#6B7280',
            'very_dark_gray': '#374151',
            'black': '#1F2937',
            'border': '#D1D5DB',
            'text_primary': '#111827',
            'text_secondary': '#6B7280',
            'text_light': '#9CA3AF'  # Fixed: removed rgba, using hex
        }

    def setup_fonts(self):
        """Configure font system"""
        self.fonts = {
            'heading': ('Segoe UI', 24, 'bold'),
            'title': ('Segoe UI', 18, 'bold'),
            'subtitle': ('Segoe UI', 16, 'bold'),
            'body': ('Segoe UI', 11),
            'body_bold': ('Segoe UI', 11, 'bold'),
            'caption': ('Segoe UI', 10),
            'small': ('Segoe UI', 9)
        }

>>>>>>> de2d156 (Initial commit)
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def restart_as_admin(self):
        try:
            result = messagebox.askyesno(
                "Administrator Privileges Required",
                "Exam Shield Pro requires administrator privileges to function properly.\\n\\n"
                "This is needed for:\\n"
                "• Advanced security monitoring\\n"
                "• System-level protection\\n"
                "• Network security controls\\n"
                "• Process management\\n\\n"
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
=======
        x = (self.root.winfo_screenwidth() // 2) - 300
        y = (self.root.winfo_screenheight() // 2) - 400
        self.root.geometry(f"600x800+{x}+{y}")
>>>>>>> de2d156 (Initial commit)

    def setup_modern_ui(self):
        # Set background
        self.root.configure(bg=self.colors['light_gray'])
        
        # Main container
        self.main_container = tk.Frame(self.root, bg=self.colors['light_gray'])
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Create sections
        self.create_header()
        self.create_content()
        self.create_footer()

    def create_header(self):
        """Create modern header"""
        header_frame = tk.Frame(self.main_container, bg=self.colors['primary'], height=180)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Header content
        header_content = tk.Frame(header_frame, bg=self.colors['primary'])
        header_content.pack(expand=True)
        
        # Logo/Icon
        icon_label = tk.Label(header_content, text="🛡️", font=('Segoe UI', 48), 
                             bg=self.colors['primary'], fg='white')
        icon_label.pack(pady=(30, 10))
        
        # Title
        title_label = tk.Label(header_content, text="EXAM SHIELD", 
                              font=self.fonts['heading'],
                              bg=self.colors['primary'], fg='white')
        title_label.pack()
        
        # Subtitle  
        subtitle_label = tk.Label(header_content, text="Professional Security Suite v2.0",
                                 font=self.fonts['body'],
                                 bg=self.colors['primary'], fg=self.colors['text_light'])  # Fixed
        subtitle_label.pack(pady=(5, 0))
        
        # Status badge
        badge_frame = tk.Frame(header_content, bg=self.colors['success'], relief=tk.FLAT)
        badge_frame.pack(pady=(15, 20))
        
        badge_text = tk.Label(badge_frame, text="✓ ADMINISTRATOR MODE ACTIVE",
                             font=self.fonts['caption'],
                             bg=self.colors['success'], fg='white',
                             padx=15, pady=8)
        badge_text.pack()

    def create_content(self):
        """Create main content area"""
        content_frame = tk.Frame(self.main_container, bg=self.colors['light_gray'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # Login card
        self.create_login_card(content_frame)
        
        # Features card
        self.create_features_card(content_frame)
        
        # Info cards
        self.create_info_cards(content_frame)

    def create_login_card(self, parent):
        """Create login form card"""
        # Card container
        login_card = tk.Frame(parent, bg=self.colors['white'], relief=tk.RAISED, bd=1)
        login_card.pack(fill=tk.X, pady=(0, 20))
        
        # Card content
        card_content = tk.Frame(login_card, bg=self.colors['white'])
        card_content.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # Title
        title_label = tk.Label(card_content, text="Secure Authentication",
                              font=self.fonts['title'],
                              bg=self.colors['white'], fg=self.colors['text_primary'])
        title_label.pack(anchor=tk.W, pady=(0, 30))
        
        # Username field
        self.create_input_field(card_content, "Username", "username")
        
        # Password field  
        self.create_input_field(card_content, "Password", "password", show="*")
        
        # Buttons
        self.create_action_buttons(card_content)

    def create_input_field(self, parent, label_text, field_type, show=None):
        """Create modern input field"""
        container = tk.Frame(parent, bg=self.colors['white'])
        container.pack(fill=tk.X, pady=(0, 20))
        
        # Label
        label = tk.Label(container, text=label_text,
                        font=self.fonts['body_bold'],
                        bg=self.colors['white'], fg=self.colors['text_primary'])
        label.pack(anchor=tk.W, pady=(0, 8))
        
        # Entry frame for border effect
        entry_frame = tk.Frame(container, bg=self.colors['border'], relief=tk.FLAT, bd=1)
        entry_frame.pack(fill=tk.X)
        
        # Entry widget
        if field_type == "username":
            self.username_var = tk.StringVar(value="admin")
            entry = tk.Entry(entry_frame, textvariable=self.username_var,
                           font=self.fonts['body'], relief=tk.FLAT, bd=0,
                           bg=self.colors['white'], fg=self.colors['text_primary'],
                           insertbackground=self.colors['primary'])
        else:  # password
            self.password_var = tk.StringVar()
            entry = tk.Entry(entry_frame, textvariable=self.password_var,
                           font=self.fonts['body'], show=show, relief=tk.FLAT, bd=0,
                           bg=self.colors['white'], fg=self.colors['text_primary'],
                           insertbackground=self.colors['primary'])
        
        entry.pack(fill=tk.X, padx=15, pady=15)
        
        # Store reference for later use
        if field_type == "username":
            self.username_entry = entry
        else:
            self.password_entry = entry

    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_container = tk.Frame(parent, bg=self.colors['white'])
        button_container.pack(fill=tk.X, pady=(10, 0))
        
        # Login button
        self.login_btn = tk.Button(button_container, text="🔐 LOGIN TO SYSTEM",
                                  command=self.login,
                                  bg=self.colors['primary'], fg='white',
                                  font=self.fonts['body_bold'],
                                  relief=tk.FLAT, bd=0, cursor='hand2',
                                  activebackground=self.colors['primary_dark'],
                                  activeforeground='white')
        self.login_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), pady=15)
        
        # Exit button
        exit_btn = tk.Button(button_container, text="❌ EXIT APPLICATION",
                            command=self.exit_app,
                            bg=self.colors['danger'], fg='white',
                            font=self.fonts['body_bold'],
                            relief=tk.FLAT, bd=0, cursor='hand2',
                            activebackground=self.colors['danger_dark'],
                            activeforeground='white')
        exit_btn.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0), pady=15)
        
        # Bind events
<<<<<<< HEAD
>>>>>>> 8516873 (Initial commit: Project version 1)
        password_entry.bind("<Return>", lambda e: self.login())
        username_entry.bind("<Return>", lambda e: password_entry.focus())
        self.root.bind("<Escape>", lambda e: self.exit_app())
=======
        self.password_entry.bind("<Return>", lambda e: self.login())
        self.username_entry.bind("<Return>", lambda e: self.password_entry.focus())
>>>>>>> de2d156 (Initial commit)
        
        # Set focus
        if self.username_var.get():
            self.password_entry.focus()
        else:
            self.username_entry.focus()

    def create_features_card(self, parent):
        """Create features showcase"""
        features_card = tk.Frame(parent, bg=self.colors['white'], relief=tk.RAISED, bd=1)
        features_card.pack(fill=tk.X, pady=(0, 20))
        
        card_content = tk.Frame(features_card, bg=self.colors['white'])
        card_content.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)
        
        # Title
        title_label = tk.Label(card_content, text="🔒 Advanced Security Features",
                              font=self.fonts['title'],
                              bg=self.colors['white'], fg=self.colors['text_primary'])
        title_label.pack(anchor=tk.W, pady=(0, 20))
        
        # Features grid
        features_frame = tk.Frame(card_content, bg=self.colors['white'])
        features_frame.pack(fill=tk.X)
        
        features = [
            ("🔤", "Keyboard Protection", "Advanced keystroke monitoring"),
            ("🖱️", "Mouse Security", "Smart button control"),
            ("🌐", "Network Shield", "Complete internet blocking"),
            ("🪟", "Window Guardian", "Real-time window protection"),
            ("🔍", "Process Monitor", "Automated threat detection"),
            ("📊", "Live Analytics", "Real-time security tracking")
        ]
        
        for i, (icon, title, desc) in enumerate(features):
            row = i // 2
            col = i % 2
            
            feature_frame = tk.Frame(features_frame, bg=self.colors['light_gray'], 
                                   relief=tk.FLAT, bd=0)
            feature_frame.grid(row=row, column=col, sticky='ew', padx=5, pady=5)
            features_frame.grid_columnconfigure(col, weight=1)
            
            # Feature content
            content = tk.Frame(feature_frame, bg=self.colors['light_gray'])
            content.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
            
            # Header
            header = tk.Frame(content, bg=self.colors['light_gray'])
            header.pack(fill=tk.X, pady=(0, 8))
            
            icon_label = tk.Label(header, text=icon, font=('Segoe UI', 16),
                                 bg=self.colors['light_gray'], fg=self.colors['primary'])
            icon_label.pack(side=tk.LEFT, padx=(0, 10))
            
            title_label = tk.Label(header, text=title,
                                  font=self.fonts['body_bold'],
                                  bg=self.colors['light_gray'], fg=self.colors['text_primary'])
            title_label.pack(side=tk.LEFT)
            
            # Description
            desc_label = tk.Label(content, text=desc,
                                 font=self.fonts['caption'],
                                 bg=self.colors['light_gray'], fg=self.colors['text_secondary'],
                                 wraplength=200, justify=tk.LEFT)
            desc_label.pack(anchor=tk.W)

    def create_info_cards(self, parent):
        """Create information cards"""
        # Emergency access card
        emergency_card = tk.Frame(parent, bg=self.colors['warning'], relief=tk.FLAT, bd=0)
        emergency_card.pack(fill=tk.X, pady=(0, 15))
        
        emergency_content = tk.Frame(emergency_card, bg=self.colors['warning'])
        emergency_content.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Label(emergency_content, text="🔑 Emergency Access",
                font=self.fonts['body_bold'],
                bg=self.colors['warning'], fg='white').pack(anchor=tk.W)
        
        tk.Label(emergency_content, 
                text="Press Ctrl+Shift+Y during lockdown to access admin panel",
                font=self.fonts['body'],
                bg=self.colors['warning'], fg='white').pack(anchor=tk.W, pady=(5, 0))
        
        # First-time setup (if applicable)
        if not self.db_manager.admin_exists():
            setup_card = tk.Frame(parent, bg=self.colors['info'], relief=tk.FLAT, bd=0)
            setup_card.pack(fill=tk.X)
            
            setup_content = tk.Frame(setup_card, bg=self.colors['info'])
            setup_content.pack(fill=tk.X, padx=20, pady=15)
            
            tk.Label(setup_content, text="ℹ️ First Time Setup",
                    font=self.fonts['body_bold'],
                    bg=self.colors['info'], fg='white').pack(anchor=tk.W)
            
            tk.Label(setup_content, 
                    text="Default credentials: admin / admin\\nChange password after first login",
                    font=self.fonts['body'],
                    bg=self.colors['info'], fg='white').pack(anchor=tk.W, pady=(5, 0))

    def create_footer(self):
        """Create footer"""
        footer_frame = tk.Frame(self.main_container, bg=self.colors['very_dark_gray'], height=60)
        footer_frame.pack(fill=tk.X)
        footer_frame.pack_propagate(False)
        
        footer_content = tk.Frame(footer_frame, bg=self.colors['very_dark_gray'])
        footer_content.pack(expand=True, pady=20)
        
        version_label = tk.Label(footer_content,
                                text="Exam Shield Pro v2.0 - Professional Security Suite",
                                font=self.fonts['caption'],
                                bg=self.colors['very_dark_gray'], fg=self.colors['text_light'])
        version_label.pack()
        
        copyright_label = tk.Label(footer_content,
                                  text="Enhanced Modern Design • Administrator Mode Active",
                                  font=self.fonts['small'],
                                  bg=self.colors['very_dark_gray'], fg=self.colors['text_light'])
        copyright_label.pack(pady=(5, 0))

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
        """Login with enhanced feedback"""
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        if not username:
<<<<<<< HEAD
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
=======
            messagebox.showerror("Validation Error", "Please enter username")
            return
        if not password:
            messagebox.showerror("Validation Error", "Please enter password")
>>>>>>> de2d156 (Initial commit)
            return
        
        # Show loading state
        original_text = self.login_btn.cget('text')
        self.login_btn.configure(text="🔄 AUTHENTICATING...", state=tk.DISABLED)
        self.root.update()
        
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
                self.login_btn.configure(text=original_text, state=tk.NORMAL)
                messagebox.showerror("Authentication Failed", "Invalid username or password")
                self.password_var.set("")
        except Exception as e:
<<<<<<< HEAD
            messagebox.showerror("Error", f"Login error: {str(e)}")
>>>>>>> 8516873 (Initial commit: Project version 1)
=======
            self.login_btn.configure(text=original_text, state=tk.NORMAL)
            messagebox.showerror("System Error", f"Login error: {str(e)}")
>>>>>>> de2d156 (Initial commit)

    def start_admin_session(self):
        """Start admin session"""
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
=======
            messagebox.showinfo("System Loaded",
                               "Exam Shield Pro loaded successfully!\\n\\n"
                               "✅ All security modules initialized\\n"
                               "✅ Admin panel ready\\n" 
                               "✅ System tray active\\n"
                               "✅ Administrator privileges confirmed\\n\\n"
                               "🔑 Emergency Access: Ctrl+Shift+Y")
>>>>>>> de2d156 (Initial commit)
        except Exception as e:
            messagebox.showerror("Startup Error", f"Failed to start: {str(e)}")
            self.root.deiconify()

    def exit_app(self):
        """Exit application"""
        if messagebox.askyesno("Exit Application", 
                              "Close Exam Shield Pro?\\n\\nThis will terminate all security features."):
            try:
<<<<<<< HEAD
                self.db_manager.log_activity("APPLICATION_EXIT", "Exam Shield closed by user")
>>>>>>> 8516873 (Initial commit: Project version 1)
=======
                self.db_manager.log_activity("APPLICATION_EXIT", "Application closed by user")
>>>>>>> de2d156 (Initial commit)
            except:
                pass
            self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    try:
        app = ModernExamShield()
        if hasattr(app, 'root'):
            app.run()
    except Exception as e:
<<<<<<< HEAD
<<<<<<< HEAD
        messagebox.showerror("Startup Error", 
                           f"Exam Shield Premium failed to start:\n{str(e)}")
=======
        messagebox.showerror("Startup Error", f"Application failed to start:\n{str(e)}")
>>>>>>> 8516873 (Initial commit: Project version 1)
=======
        messagebox.showerror("Startup Error", f"Application failed to start:\\n{str(e)}")
>>>>>>> de2d156 (Initial commit)
