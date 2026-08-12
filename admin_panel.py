<<<<<<< HEAD
"""
<<<<<<< HEAD
Admin Panel for Exam Shield - COMPLETE STABLE VERSION
All methods properly defined to eliminate attribute errors
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog, filedialog
=======
Admin Panel for Exam Shield - ENHANCED WITH SELECTIVE CONTROLS
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
>>>>>>> 8516873 (Initial commit: Project version 1)
import threading
import json
from datetime import datetime
import keyboard
from pynput import mouse
<<<<<<< HEAD
import theme
=======
>>>>>>> 8516873 (Initial commit: Project version 1)

class AdminPanel:
    def __init__(self, db_manager, security_manager, parent_window):
        self.db_manager = db_manager
        self.security_manager = security_manager
        self.parent_window = parent_window
<<<<<<< HEAD
        self.security_manager.set_admin_panel(self)

=======
=======
import tkinter as tk
from tkinter import messagebox
import sys
import os
import hashlib
import ctypes
import subprocess
from database_manager import DatabaseManager
try:
    from admin_panel import AdminPanel
    from security_manager import SecurityManager
    from system_tray import SystemTray
    import threading
except ImportError:
    print("Note: Some modules may not be available, but main UI will work")

class AdminPanel:
    def __init__(self):
        if not self.is_admin():
            self.restart_as_admin()
            return
            
        self.root = tk.Tk()
        self.root.title("Exam Shield Pro v2.0 - Modern Design")
        self.root.geometry("550x700")
        self.root.resizable(False, False)
>>>>>>> de2d156 (Initial commit)
        
        # Safe color palette - using only standard colors
        self.colors = {
            'primary': '#2563EB',      # Blue
            'primary_dark': '#1E40AF',
            'success': '#059669',       # Green
            'danger': '#DC2626',        # Red
            'warning': '#D97706',       # Orange
            'white': '#FFFFFF',
            'light': '#F8FAFC',        # Very light gray
            'gray': '#6B7280',         # Medium gray
            'dark': '#374151',         # Dark gray
            'black': '#111827'         # Very dark
        }
        
<<<<<<< HEAD
        # NEW: Key/Mouse detection variables
>>>>>>> 8516873 (Initial commit: Project version 1)
        self.detecting_key = False
        self.detecting_mouse = False
        self.detected_key = None
        self.mouse_listener = None
<<<<<<< HEAD

        self.window = tk.Toplevel()
        self.window.title("Exam Shield Premium - Admin Panel v2.0")
        self.window.geometry("950x750")
        self.window.resizable(True, True)

        self.current_theme = "light"
        self.load_theme(self.current_theme)

=======
=======
        try:
            self.db_manager = DatabaseManager()
        except:
            # Create a dummy database manager for UI testing
            class DummyDB:
                def admin_exists(self): return False
                def verify_admin(self, u, p): return u == "admin" and hashlib.sha256("admin".encode()).hexdigest() == p
                def log_activity(self, action, details): pass
            self.db_manager = DummyDB()
>>>>>>> de2d156 (Initial commit)
        
        self.security_manager = None
        self.system_tray = None
        
<<<<<<< HEAD
>>>>>>> 8516873 (Initial commit: Project version 1)
        self.setup_window()
=======
>>>>>>> de2d156 (Initial commit)
        self.setup_ui()
        self.center_window()

<<<<<<< HEAD
<<<<<<< HEAD
    def load_theme(self, theme_name):
        t = theme.get_theme(theme_name)
        tc = t.colors
        if theme_name == "light":
            self.colors = {
                'primary': '#1e3d59','secondary': '#17223b','accent': '#ffc947','success': '#27ae60',
                'warning': '#f39c12','danger': '#e74c3c','info': '#3498db','surface': '#f8f9fa',
                'card': '#ffffff','text_primary': '#2c3e50','text_secondary': '#7f8c8d'
            }
        else:
            self.colors = {
                'primary': tc['primary'],'secondary': tc['secondary'],'accent': tc['warning'],'success': tc['success'],
                'warning': tc['warning'],'danger': tc['danger'],'info': tc['info'],'surface': tc['surface'],
                'card': tc['card'],'text_primary': tc['text_primary'],'text_secondary': tc['text_secondary']
            }
        self.window.configure(bg=self.colors['surface'])

    def change_theme(self, event=None):
        self.current_theme = self.theme_var.get()
        self.load_theme(self.current_theme)
        for widget in self.window.winfo_children():
            widget.destroy()
        self.setup_ui()

    def setup_window(self):
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - 475
        y = (self.window.winfo_screenheight() // 2) - 375
        self.window.geometry(f"950x750+{x}+{y}")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        try:
            self.window.withdraw()
        except Exception as e:
            try:
                messagebox.showerror("Error", f"Failed to close panel: {e}")
            finally:
                self.window.withdraw()

    def show(self):
        self.window.deiconify()
        self.window.lift()
        self.refresh_status()

    def setup_ui(self):
        style = ttk.Style(); style.theme_use('clam')
        style.configure('TNotebook', background=self.colors['surface'])
        style.configure('TNotebook.Tab', padding=[15, 8], font=('Segoe UI', 10, 'bold'))

        header_frame = tk.Frame(self.window, bg=self.colors['primary'], height=60)
        header_frame.pack(fill=tk.X); header_frame.pack_propagate(False)
        hc = tk.Frame(header_frame, bg=self.colors['primary']); hc.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        tk.Label(hc, text="🛡️ EXAM SHIELD PREMIUM", font=("Segoe UI", 16, "bold"), bg=self.colors['primary'], fg=self.colors['card']).pack(side=tk.LEFT)
        tk.Label(hc, text="v2.0 Administrative Control Center", font=("Segoe UI", 9), bg=self.colors['primary'], fg=self.colors['accent']).pack(side=tk.RIGHT)

        self.notebook = ttk.Notebook(self.window); self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.create_control_tab(); self.create_monitoring_tab(); self.create_settings_tab(); self.create_logs_tab()

    def create_control_tab(self):
        frame = ttk.Frame(self.notebook); self.notebook.add(frame, text="📋 Control Center")
        main = tk.Frame(frame, bg=self.colors['surface']); main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Status
        status_card = tk.Frame(main, bg=self.colors['card']); status_card.pack(fill=tk.X, pady=(0,10))
        sh = tk.Frame(status_card, bg=self.colors['info'], height=40); sh.pack(fill=tk.X); sh.pack_propagate(False)
        tk.Label(sh, text="📊 System Status", font=("Segoe UI", 12, "bold"), bg=self.colors['info'], fg=self.colors['card']).pack(pady=10)
        sc = tk.Frame(status_card, bg=self.colors['card']); sc.pack(fill=tk.X, padx=15, pady=15)
        self.status_label = tk.Label(sc, text="🔓 Exam Mode: INACTIVE", font=("Segoe UI", 14, "bold"), bg=self.colors['card'], fg=self.colors['success']); self.status_label.pack(anchor=tk.W)
        self.system_info_label = tk.Label(sc, text="System Info Loading...", font=("Segoe UI", 10), bg=self.colors['card'], fg=self.colors['text_secondary']); self.system_info_label.pack(anchor=tk.W, pady=(5,0))
        ind = tk.Frame(sc, bg=self.colors['card']); ind.pack(anchor=tk.W, pady=(5,0), fill=tk.X)
        tk.Label(ind, text="Security Modules:", font=("Segoe UI", 10, "bold"), bg=self.colors['card'], fg=self.colors['text_primary']).pack(anchor=tk.W)
        row = tk.Frame(ind, bg=self.colors['card']); row.pack(anchor=tk.W, pady=(2,0))
        self.keyboard_status = tk.Label(row, text="⚫ Keyboard", font=("Segoe UI", 9), bg=self.colors['card'], fg=self.colors['text_secondary']); self.keyboard_status.pack(side=tk.LEFT, padx=(0,15))
        self.mouse_status = tk.Label(row, text="⚫ Mouse", font=("Segoe UI", 9), bg=self.colors['card'], fg=self.colors['text_secondary']); self.mouse_status.pack(side=tk.LEFT, padx=(0,15))
        self.network_status = tk.Label(row, text="⚫ Network", font=("Segoe UI", 9), bg=self.colors['card'], fg=self.colors['text_secondary']); self.network_status.pack(side=tk.LEFT, padx=(0,15))
        self.window_status = tk.Label(row, text="⚫ Windows", font=("Segoe UI", 9), bg=self.colors['card'], fg=self.colors['text_secondary']); self.window_status.pack(side=tk.LEFT, padx=(0,15))

        # Controls
        card = tk.Frame(main, bg=self.colors['card']); card.pack(fill=tk.X, pady=(0,10))
        ch = tk.Frame(card, bg=self.colors['primary'], height=40); ch.pack(fill=tk.X); ch.pack_propagate(False)
        tk.Label(ch, text="🎯 Exam Controls", font=("Segoe UI", 12, "bold"), bg=self.colors['primary'], fg=self.colors['card']).pack(pady=10)
        btns = tk.Frame(card, bg=self.colors['card']); btns.pack(fill=tk.X, padx=15, pady=15)
        self.start_btn = tk.Button(btns, text="🔒 START SELECTIVE LOCKDOWN", command=self.show_selective_lockdown_dialog, bg=self.colors['primary'], fg=self.colors['card'], font=("Segoe UI", 11, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=10); self.start_btn.pack(side=tk.LEFT, padx=(0,10))
        self.stop_btn = tk.Button(btns, text="🔓 END LOCKDOWN MODE", command=self.stop_exam_mode, state=tk.DISABLED, bg=self.colors['warning'], fg=self.colors['card'], font=("Segoe UI", 11, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=10); self.stop_btn.pack(side=tk.LEFT, padx=(0,10))
        tk.Button(btns, text="🚨 EMERGENCY STOP", command=self.emergency_stop, bg=self.colors['danger'], fg=self.colors['card'], font=("Segoe UI", 11, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=10).pack(side=tk.RIGHT)

        self.create_individual_controls(main)

    def create_individual_controls(self, parent):
        card = tk.Frame(parent, bg=self.colors['card']); card.pack(fill=tk.X, pady=(0,10))
        ch = tk.Frame(card, bg=self.colors['secondary'], height=40); ch.pack(fill=tk.X); ch.pack_propagate(False)
        tk.Label(ch, text="🛠️ Individual Security Controls", font=("Segoe UI", 12, "bold"), bg=self.colors['secondary'], fg=self.colors['card']).pack(pady=10)
        cont = tk.Frame(card, bg=self.colors['card']); cont.pack(fill=tk.X, padx=15, pady=15)
        row1 = tk.Frame(cont, bg=self.colors['card']); row1.pack(fill=tk.X, pady=(0,5))
        tk.Button(row1, text="🖱️ Mouse Blocker", command=self.show_mouse_controls, bg=self.colors['info'], fg=self.colors['card'], font=("Segoe UI", 10, "bold"), relief=tk.FLAT, cursor='hand2', padx=15, pady=8).pack(side=tk.LEFT, padx=(0,10))
        tk.Button(row1, text="🌐 Internet Blocker", command=self.show_network_controls, bg=self.colors['info'], fg=self.colors['card'], font=("Segoe UI", 10, "bold"), relief=tk.FLAT, cursor='hand2', padx=15, pady=8).pack(side=tk.LEFT, padx=(0,10))
        tk.Button(row1, text="🪟 Window Guardian", command=self.show_window_controls, bg=self.colors['info'], fg=self.colors['card'], font=("Segoe UI", 10, "bold"), relief=tk.FLAT, cursor='hand2', padx=15, pady=8).pack(side=tk.LEFT)

    # ===== SELECTIVE LOCKDOWN DIALOG (FIXED) =====
    def show_selective_lockdown_dialog(self):
        dialog = tk.Toplevel(self.window)
        dialog.title("🔒 Selective Lockdown Configuration")
        dialog.geometry("500x600")
        dialog.configure(bg=self.colors['surface'])
        dialog.transient(self.window)
        dialog.grab_set()

=======
    def setup_window(self):
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (475)
        y = (self.window.winfo_screenheight() // 2) - (375)
        self.window.geometry(f"950x750+{x}+{y}")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
=======
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return True  # For testing purposes

    def restart_as_admin(self):
        try:
            result = messagebox.askyesno(
                "Administrator Required",
                "Exam Shield requires administrator privileges.\\n\\n"
                "Click 'Yes' to restart with admin privileges."
            )
            
            if result:
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, f'"{os.path.abspath(__file__)}"', None, 1
                )
                sys.exit(0)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get admin privileges: {e}")
            sys.exit(1)

    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - 275
        y = (self.root.winfo_screenheight() // 2) - 350
        self.root.geometry(f"550x700+{x}+{y}")
>>>>>>> de2d156 (Initial commit)

    def setup_ui(self):
        # Main background
        self.root.configure(bg=self.colors['light'])
        
        # Header
        header_frame = tk.Frame(self.root, bg=self.colors['primary'], height=140)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Shield icon and title
        tk.Label(header_frame, text="🛡️", font=('Arial', 40), 
                bg=self.colors['primary'], fg='white').pack(pady=(20, 5))
        
        tk.Label(header_frame, text="EXAM SHIELD PRO", 
                font=('Arial', 20, 'bold'),
                bg=self.colors['primary'], fg='white').pack()
        
        tk.Label(header_frame, text="Modern Security Suite v2.0", 
                font=('Arial', 10),
                bg=self.colors['primary'], fg='white').pack(pady=(5, 20))
        
        # Main content
        content_frame = tk.Frame(self.root, bg=self.colors['light'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Login card
        login_card = tk.Frame(content_frame, bg=self.colors['white'], 
                             relief=tk.RAISED, bd=2)
        login_card.pack(fill=tk.X, pady=(0, 20))
        
<<<<<<< HEAD
        indicators_frame = ttk.Frame(self.security_status_frame)
        indicators_frame.pack(anchor=tk.W, pady=(2, 0))
        
        self.keyboard_status = ttk.Label(indicators_frame, text="⚫ Keyboard", foreground="gray")
        self.keyboard_status.pack(side=tk.LEFT, padx=(0, 15))
        
        self.mouse_status = ttk.Label(indicators_frame, text="⚫ Mouse", foreground="gray")
        self.mouse_status.pack(side=tk.LEFT, padx=(0, 15))
        
        self.network_status = ttk.Label(indicators_frame, text="⚫ Network", foreground="gray")
        self.network_status.pack(side=tk.LEFT, padx=(0, 15))
        
        self.window_status = ttk.Label(indicators_frame, text="⚫ Windows", foreground="gray")
        self.window_status.pack(side=tk.LEFT, padx=(0, 15))
        
        # Control buttons
        control_buttons_frame = ttk.LabelFrame(control_frame, text="Exam Controls", padding="10")
        control_buttons_frame.pack(fill=tk.X, padx=10, pady=5)
        
        button_frame = ttk.Frame(control_buttons_frame)
        button_frame.pack(fill=tk.X)
        
        # NEW: Changed to selective lockdown
        self.start_btn = ttk.Button(button_frame, text="🔒 START SELECTIVE LOCKDOWN", 
                                   command=self.show_selective_lockdown_dialog, style="Accent.TButton")
        self.start_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_btn = ttk.Button(button_frame, text="🔓 END LOCKDOWN MODE",
                                  command=self.stop_exam_mode, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.emergency_btn = ttk.Button(button_frame, text="🚨 EMERGENCY STOP",
                                       command=self.emergency_stop)
        self.emergency_btn.pack(side=tk.RIGHT)
        
        # Individual feature controls (same as before)
        self.create_individual_controls(control_frame)
        
        # Threat detection
        threat_frame = ttk.LabelFrame(control_frame, text="Threat Detection", padding="10")
        threat_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.threat_label = ttk.Label(threat_frame, text="No threats detected", foreground="green")
        self.threat_label.pack(anchor=tk.W)

    def create_individual_controls(self, parent):
        """Create individual security controls"""
        features_frame = ttk.LabelFrame(parent, text="Individual Security Controls", padding="10")
        features_frame.pack(fill=tk.X, padx=10, pady=5)
        
        feature_btn_frame1 = ttk.Frame(features_frame)
        feature_btn_frame1.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Button(feature_btn_frame1, text="🖱️ Mouse Blocker",
                  command=self.show_mouse_controls).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(feature_btn_frame1, text="🌐 Internet Blocker",
                  command=self.show_network_controls).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(feature_btn_frame1, text="🪟 Window Guardian",
                  command=self.show_window_controls).pack(side=tk.LEFT, padx=(0, 5))
        
        feature_btn_frame2 = ttk.Frame(features_frame)
        feature_btn_frame2.pack(fill=tk.X)
        
        ttk.Button(feature_btn_frame2, text="📊 Live Monitor",
                  command=lambda: self.notebook.select(1)).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(feature_btn_frame2, text="⚙️ Settings",
                  command=lambda: self.notebook.select(2)).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(feature_btn_frame2, text="🔄 Refresh Status",
                  command=self.refresh_status).pack(side=tk.LEFT, padx=(0, 5))

    # NEW: Selective Lockdown Dialog
    def show_selective_lockdown_dialog(self):
        """Show dialog for selective lockdown options"""
        dialog = tk.Toplevel(self.window)
        dialog.title("🔒 Selective Lockdown Configuration")
        dialog.geometry("500x600")
        dialog.transient(self.window)
        dialog.grab_set()
        
        # Center dialog
>>>>>>> 8516873 (Initial commit: Project version 1)
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - 250
        y = (dialog.winfo_screenheight() // 2) - 300
        dialog.geometry(f"500x600+{x}+{y}")
<<<<<<< HEAD

        header = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text="🔒 Select Security Modules to Activate",
                font=("Segoe UI", 14, "bold"), bg=self.colors['primary'], 
                fg=self.colors['card']).pack(pady=20)

        options = tk.Frame(dialog, bg=self.colors['surface'])
        options.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)

        self.selective_vars = {}
=======
=======
        # Card content
        card_content = tk.Frame(login_card, bg=self.colors['white'])
        card_content.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
>>>>>>> de2d156 (Initial commit)
        
        # Title
        tk.Label(card_content, text="🔐 Secure Login", 
                font=('Arial', 16, 'bold'),
                bg=self.colors['white'], fg=self.colors['black']).pack(pady=(0, 20))
        
        # Username
        tk.Label(card_content, text="Username:", 
                font=('Arial', 11, 'bold'),
                bg=self.colors['white'], fg=self.colors['dark']).pack(anchor='w')
        
        self.username_var = tk.StringVar(value="admin")
        username_entry = tk.Entry(card_content, textvariable=self.username_var,
                                 font=('Arial', 12), width=35, relief=tk.SOLID, bd=1)
        username_entry.pack(fill=tk.X, pady=(5, 15), ipady=8)
        
<<<<<<< HEAD
>>>>>>> 8516873 (Initial commit: Project version 1)
        modules = [
            ("keyboard", "🔤 Keyboard Shortcuts Blocking", "Block Alt+Tab, Ctrl+Alt+Del, etc."),
            ("mouse", "🖱️ Mouse Button Restrictions", "Block middle, back, forward buttons"),
            ("internet", "🌐 Internet Access Blocking", "Complete internet disconnection"),
            ("windows", "🪟 Window Protection", "Prevent closing/minimizing windows"),
            ("processes", "🔍 Process Monitoring", "Auto-terminate suspicious processes")
        ]
<<<<<<< HEAD

        for key, title, desc in modules:
            card = tk.Frame(options, bg=self.colors['card'], relief=tk.FLAT, bd=1)
            card.pack(fill=tk.X, pady=(0, 10))
            content = tk.Frame(card, bg=self.colors['card'])
            content.pack(fill=tk.X, padx=15, pady=12)
            var = tk.BooleanVar(value=True)
            self.selective_vars[key] = var
            tk.Checkbutton(content, text=title, variable=var,
                         font=("Segoe UI", 11, "bold"), bg=self.colors['card'],
                         fg=self.colors['text_primary'], selectcolor=self.colors['card'],
                         activebackground=self.colors['card']).pack(anchor=tk.W)
            tk.Label(content, text=desc, font=("Segoe UI", 9), bg=self.colors['card'],
                    fg=self.colors['text_secondary']).pack(anchor=tk.W, padx=20, pady=(2,0))

        btns = tk.Frame(dialog, bg=self.colors['surface'])
        btns.pack(fill=tk.X, padx=40, pady=20)
        tk.Button(btns, text="🚀 START SELECTED LOCKDOWN",
                 command=lambda: self.start_selective_lockdown(dialog),
                 bg=self.colors['success'], fg=self.colors['card'], 
                 font=("Segoe UI", 11, "bold"), relief=tk.FLAT, pady=10, cursor='hand2').pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,10))
        tk.Button(btns, text="❌ CANCEL", command=dialog.destroy,
                 bg=self.colors['danger'], fg=self.colors['card'], 
                 font=("Segoe UI", 11, "bold"), relief=tk.FLAT, pady=10, cursor='hand2').pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10,0))

    def start_selective_lockdown(self, dialog):
        selected = {key: var.get() for key, var in self.selective_vars.items()}
        if not any(selected.values()):
            messagebox.showwarning("No Selection", "Please select at least one security module!")
            return
        names = [key.title() for key, s in selected.items() if s]
        if messagebox.askyesno("Confirm Selective Lockdown", "Start lockdown with these modules?\n\n" + "\n".join(f"✓ {n}" for n in names)):
            dialog.destroy()
            try:
                self.security_manager.start_exam_mode(selected)
                self.start_btn.config(state=tk.DISABLED)
                self.stop_btn.config(state=tk.NORMAL)
                self.refresh_status()
                messagebox.showinfo("🔒 SELECTIVE LOCKDOWN ACTIVE", "Lockdown active with:\n" + "\n".join(f"✓ {n}" for n in names))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to start lockdown: {e}")

    # ===== MONITORING TAB =====
    def create_monitoring_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📊 Live Monitor")
        container = tk.Frame(frame, bg=self.colors['surface']); container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        header = tk.Frame(container, bg=self.colors['info'], height=50); header.pack(fill=tk.X); header.pack_propagate(False)
        tk.Label(header, text="📊 Real-time Security Events", font=("Segoe UI", 14, "bold"), bg=self.colors['info'], fg=self.colors['card']).pack(pady=15)
        content = tk.Frame(container, bg=self.colors['card']); content.pack(fill=tk.BOTH, expand=True, pady=(10,0))
        columns = ("Time","Severity","Action","Details","Status")
        self.activity_tree = ttk.Treeview(content, columns=columns, show="headings", height=20)
        for col in columns: self.activity_tree.heading(col, text=col)
        self.activity_tree.column("Time", width=120); self.activity_tree.column("Severity", width=80); self.activity_tree.column("Action", width=180); self.activity_tree.column("Details", width=300); self.activity_tree.column("Status", width=100)
        sb = ttk.Scrollbar(content, orient=tk.VERTICAL, command=self.activity_tree.yview); self.activity_tree.configure(yscrollcommand=sb.set)
        self.activity_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20); sb.pack(side=tk.RIGHT, fill=tk.Y, padx=(0,20), pady=20)
=======
=======
        # Password  
        tk.Label(card_content, text="Password:", 
                font=('Arial', 11, 'bold'),
                bg=self.colors['white'], fg=self.colors['dark']).pack(anchor='w')
>>>>>>> de2d156 (Initial commit)
        
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(card_content, textvariable=self.password_var,
                                 font=('Arial', 12), width=35, show="*", 
                                 relief=tk.SOLID, bd=1)
        password_entry.pack(fill=tk.X, pady=(5, 20), ipady=8)
        
        # Buttons
        button_frame = tk.Frame(card_content, bg=self.colors['white'])
        button_frame.pack(fill=tk.X)
        
        self.login_btn = tk.Button(button_frame, text="🔓 LOGIN", 
                                  command=self.login,
                                  bg=self.colors['primary'], fg='white',
                                  font=('Arial', 12, 'bold'),
                                  relief=tk.FLAT, cursor='hand2',
                                  width=18, pady=10)
        self.login_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        exit_btn = tk.Button(button_frame, text="❌ EXIT", 
                            command=self.exit_app,
                            bg=self.colors['danger'], fg='white',
                            font=('Arial', 12, 'bold'),
                            relief=tk.FLAT, cursor='hand2',
                            width=18, pady=10)
        exit_btn.pack(side=tk.RIGHT)
        
        # Features section
        features_card = tk.Frame(content_frame, bg=self.colors['white'], 
                                relief=tk.RAISED, bd=2)
        features_card.pack(fill=tk.X, pady=(0, 20))
        
        features_content = tk.Frame(features_card, bg=self.colors['white'])
        features_content.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        tk.Label(features_content, text="🔒 Security Features", 
                font=('Arial', 14, 'bold'),
                bg=self.colors['white'], fg=self.colors['black']).pack(pady=(0, 15))
        
        features = [
            "🔤 Advanced Keyboard Protection",
            "🖱️ Smart Mouse Control System", 
            "🌐 Complete Network Blocking",
            "🪟 Real-time Window Guardian",
            "🔍 Intelligent Process Monitor",
            "📊 Live Security Analytics"
        ]
        
        for feature in features:
            tk.Label(features_content, text=feature, 
                    font=('Arial', 10),
                    bg=self.colors['white'], fg=self.colors['gray'],
                    anchor='w').pack(fill=tk.X, pady=2)
        
        # Status section
        status_card = tk.Frame(content_frame, bg=self.colors['success'], 
                              relief=tk.FLAT, bd=0)
        status_card.pack(fill=tk.X)
        
        status_content = tk.Frame(status_card, bg=self.colors['success'])
        status_content.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Label(status_content, text="✅ Administrator Mode Active", 
                font=('Arial', 11, 'bold'),
                bg=self.colors['success'], fg='white').pack(anchor='w')
        
        tk.Label(status_content, text="Emergency Access: Ctrl+Shift+Y", 
                font=('Arial', 10),
                bg=self.colors['success'], fg='white').pack(anchor='w', pady=(5, 0))
        
        # Bind events
        password_entry.bind("<Return>", lambda e: self.login())
        username_entry.bind("<Return>", lambda e: password_entry.focus())
        self.root.bind("<Escape>", lambda e: self.exit_app())
        
        # Set focus
        if self.username_var.get():
            password_entry.focus()
        else:
            username_entry.focus()

    def login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        if not username or not password:
            messagebox.showerror("Input Error", "Please enter both username and password")
            return
        
        # Show loading
        self.login_btn.configure(text="🔄 Logging in...", state=tk.DISABLED)
        self.root.update()
        
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            if self.db_manager.verify_admin(username, password_hash):
                self.start_admin_session()
            else:
                messagebox.showerror("Login Failed", "Invalid credentials!")
                self.password_var.set("")
        except Exception as e:
            messagebox.showerror("Error", f"Login error: {str(e)}")
        finally:
            self.login_btn.configure(text="🔓 LOGIN", state=tk.NORMAL)

    def start_admin_session(self):
        try:
            self.root.withdraw()
            
            # Try to start full system
            try:
                self.security_manager = SecurityManager(self.db_manager)
                self.db_manager.log_activity("ADMIN_LOGIN", "Admin session started")
                
                admin_panel = AdminPanel(self.db_manager, self.security_manager, self.root)
                
                self.system_tray = SystemTray(admin_panel, self.security_manager)
                tray_thread = threading.Thread(target=self.system_tray.run, daemon=True)
                tray_thread.start()
                
            except Exception as module_error:
                # If modules aren't available, show a demo message
                messagebox.showinfo("Demo Mode", 
                                   f"Login successful!\\n\\n"
                                   f"Note: Full admin panel not available\\n"
                                   f"Reason: {str(module_error)[:100]}\\n\\n"
                                   f"This is a UI demo version.")
                self.root.deiconify()
                return
            
            messagebox.showinfo("Success", 
                               "🔒 Exam Shield Pro Activated!\\n\\n"
                               "✅ Admin panel loaded\\n"
                               "✅ Security systems ready\\n"
                               "✅ System tray active\\n\\n"
                               "Emergency access: Ctrl+Shift+Y")
            
        except Exception as e:
            messagebox.showerror("Startup Error", f"Failed to start admin session:\\n{str(e)}")
            self.root.deiconify()

    def exit_app(self):
        if messagebox.askyesno("Exit", "Close Exam Shield Pro?"):
            try:
                self.db_manager.log_activity("APP_EXIT", "Application closed")
            except:
                pass
            self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    try:
        app = ExamShieldModern()
        if hasattr(app, 'root'):
            app.run()
    except Exception as e:
        print(f"Startup error: {e}")
        import traceback
        traceback.print_exc()
        
<<<<<<< HEAD
        if filename:
            try:
                logs = self.db_manager.get_activity_logs(1000)
                if filename.endswith('.csv'):
                    with open(filename, 'w', newline='') as f:
                        f.write("Timestamp,Action,Details,Status\n")
                        for log in logs:
                            action, details, timestamp, blocked = log
                            status = "BLOCKED" if blocked else "ALLOWED"
                            details_clean = details if details else "N/A"
                            f.write(f'"{timestamp}","{action}","{details_clean}","{status}"\n')
                else:
                    with open(filename, 'w') as f:
                        f.write("EXAM SHIELD SECURITY LOGS\n")
                        f.write("=" * 50 + "\n")
                        f.write(f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                        f.write(f"Total Entries: {len(logs)}\n")
                        f.write("=" * 50 + "\n\n")
                        
                        for log in logs:
                            action, details, timestamp, blocked = log
                            status = "BLOCKED" if blocked else "ALLOWED"
                            f.write(f"[{timestamp}] {status}: {action}\n")
                            f.write(f"Details: {details or 'No additional details'}\n\n")
                
                messagebox.showinfo("✅ Success", f"Logs exported successfully to:\n{filename}")
            except Exception as e:
                messagebox.showerror("❌ Error", f"Export failed: {str(e)}")

    def start_auto_refresh(self):
        def refresh_loop():
            while True:
                try:
                    if self.window.winfo_exists():
                        self.window.after(0, self.refresh_status)
                        if hasattr(self, 'activity_tree'):
                            self.window.after(0, self.update_activity_feed)
                    threading.Event().wait(2)
                except:
                    break
        
        refresh_thread = threading.Thread(target=refresh_loop, daemon=True)
        refresh_thread.start()
>>>>>>> 8516873 (Initial commit: Project version 1)

    def update_activity_feed(self):
        try:
            for item in self.activity_tree.get_children():
                self.activity_tree.delete(item)
<<<<<<< HEAD
            logs = self.db_manager.get_activity_logs(20)
            for log in logs:
                action, details, timestamp, blocked = log
                status = "🚫 BLOCKED" if blocked else "✅ ALLOWED"
                if blocked or "SUSPICIOUS" in action: severity = "🔴 HIGH"
                elif "BLOCKED" in action: severity = "🟡 MED"
                else: severity = "🟢 LOW"
                try:
                    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                    time_str = dt.strftime("%H:%M:%S")
                except: time_str = timestamp
                self.activity_tree.insert("", 0, values=(time_str, severity, action, details or "No details", status))
        except Exception: pass

    # ===== SETTINGS TAB =====
    def create_settings_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="⚙️ Settings")
        container = tk.Frame(frame, bg=self.colors['surface']); container.pack(fill=tk.BOTH, expand=True)
        canvas = tk.Canvas(container, bg=self.colors['surface'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        inner = tk.Frame(canvas, bg=self.colors['surface'])
        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0), window=inner, anchor="nw"); canvas.configure(yscrollcommand=scrollbar.set)
        
        # Settings content
        settings_card = tk.Frame(inner, bg=self.colors['card']); settings_card.pack(fill=tk.X, padx=10, pady=10)
        header = tk.Frame(settings_card, bg=self.colors['success'], height=40); header.pack(fill=tk.X); header.pack_propagate(False)
        tk.Label(header, text="🔧 Advanced Settings", font=("Segoe UI", 12, "bold"), bg=self.colors['success'], fg=self.colors['card']).pack(pady=10)
        content = tk.Frame(settings_card, bg=self.colors['card']); content.pack(fill=tk.X, padx=15, pady=15)
        
        self.auto_start_var = tk.BooleanVar()
        tk.Checkbutton(content, text="Auto-start lockdown mode on login", variable=self.auto_start_var, font=("Segoe UI", 10), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['card'], activebackground=self.colors['card']).pack(anchor=tk.W)
        self.window_protection_var = tk.BooleanVar(value=True)
        tk.Checkbutton(content, text="Enable aggressive window protection", variable=self.window_protection_var, font=("Segoe UI", 10), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['card'], activebackground=self.colors['card']).pack(anchor=tk.W)
        self.process_monitoring_var = tk.BooleanVar(value=True)
        tk.Checkbutton(content, text="Enable unauthorized process termination", variable=self.process_monitoring_var, font=("Segoe UI", 10), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['card'], activebackground=self.colors['card']).pack(anchor=tk.W)
        
        # Theme Setting
        theme_frame = tk.Frame(content, bg=self.colors['card'])
        theme_frame.pack(anchor=tk.W, pady=(15, 0))
        tk.Label(theme_frame, text="Admin Panel Theme:", bg=self.colors['card'], fg=self.colors['text_primary'], font=("Segoe UI", 10)).pack(side=tk.LEFT)
        if hasattr(self, 'theme_var'):
            current = self.theme_var.get()
        else:
            current = self.current_theme
        self.theme_var = tk.StringVar(value=current)
        theme_combo = ttk.Combobox(theme_frame, textvariable=self.theme_var, values=["light", "dark", "pink"], state="readonly", width=15)
        theme_combo.pack(side=tk.LEFT, padx=10)
        theme_combo.bind("<<ComboboxSelected>>", self.change_theme)

        tk.Button(content, text="💾 Save All Settings", command=self.save_settings, bg=self.colors['primary'], fg=self.colors['card'], font=("Segoe UI", 11, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=10).pack(pady=(20,0))
        
        canvas.pack(side="left", fill="both", expand=True, padx=15, pady=15); scrollbar.pack(side="right", fill="y", padx=(0,15), pady=15)

    def save_settings(self):
        try:
            messagebox.showinfo("✅ Success", "Settings saved successfully!")
        except Exception as e:
            messagebox.showerror("❌ Error", f"Failed to save settings: {e}")

    # ===== LOGS TAB =====
    def create_logs_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📋 Security Logs")
        container = tk.Frame(frame, bg=self.colors['surface']); container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        controls = tk.Frame(container, bg=self.colors['card'], height=60); controls.pack(fill=tk.X, pady=(0,10)); controls.pack_propagate(False)
        row = tk.Frame(controls, bg=self.colors['card']); row.pack(fill=tk.X, padx=15, pady=15)
        tk.Button(row, text="🔄 Refresh", command=self.refresh_logs, bg=self.colors['info'], fg=self.colors['card'], font=("Segoe UI", 9, "bold"), relief=tk.FLAT, cursor='hand2', padx=10, pady=5).pack(side=tk.LEFT, padx=(0,10))
        tk.Button(row, text="🗑️ Clear All", command=self.clear_logs, bg=self.colors['warning'], fg=self.colors['card'], font=("Segoe UI", 9, "bold"), relief=tk.FLAT, cursor='hand2', padx=10, pady=5).pack(side=tk.LEFT, padx=(0,10))
        tk.Button(row, text="💾 Export", command=self.export_logs, bg=self.colors['success'], fg=self.colors['card'], font=("Segoe UI", 9, "bold"), relief=tk.FLAT, cursor='hand2', padx=10, pady=5).pack(side=tk.LEFT, padx=(0,10))
        
        self.log_filter_var = tk.StringVar()
        tk.Label(row, text="Filter:", font=("Segoe UI", 9, "bold"), bg=self.colors['card'], fg=self.colors['text_primary']).pack(side=tk.LEFT, padx=(20,5))
        filter_combo = ttk.Combobox(row, textvariable=self.log_filter_var, values=["All", "Blocked Only", "Security Events"], font=("Segoe UI", 9))
        filter_combo.set("All"); filter_combo.pack(side=tk.LEFT, padx=(0,10))
        filter_combo.bind("<<ComboboxSelected>>", lambda e: self.refresh_logs())
        
        logs_card = tk.Frame(container, bg=self.colors['card']); logs_card.pack(fill=tk.BOTH, expand=True)
        header = tk.Frame(logs_card, bg=self.colors['danger'], height=40); header.pack(fill=tk.X); header.pack_propagate(False)
        tk.Label(header, text="📋 Security Activity History", font=("Segoe UI", 12, "bold"), bg=self.colors['danger'], fg=self.colors['card']).pack(pady=10)
        content = tk.Frame(logs_card, bg=self.colors['card']); content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.logs_text = scrolledtext.ScrolledText(content, wrap=tk.WORD, height=25, font=("Consolas", 9), bg=self.colors['surface'], fg=self.colors['text_primary'])
        self.logs_text.pack(fill=tk.BOTH, expand=True)

    def refresh_logs(self):
        try:
            logs = self.db_manager.get_activity_logs(100)
        except Exception:
            logs = []
        self.logs_text.delete(1.0, tk.END)
        for log in logs:
            try:
                action, details, timestamp, blocked = log
                status = "BLOCKED" if blocked else "ALLOWED"
                self.logs_text.insert(tk.END, f"[{timestamp}] {action}: {details or 'N/A'} - {status}\n")
            except Exception:
                continue
        self.logs_text.see(tk.END)

    def clear_logs(self):
        self.logs_text.delete(1.0, tk.END)
        messagebox.showinfo("✅ Success", "Logs cleared!")

    def export_logs(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(self.logs_text.get(1.0, tk.END))
                messagebox.showinfo("✅ Success", f"Logs exported to:\n{filename}")
            except Exception as e:
                messagebox.showerror("❌ Error", f"Export failed: {e}")

    # ===== MOUSE CONTROLS =====
    def show_mouse_controls(self):
        win = tk.Toplevel(self.window); win.title("🖱️ Mouse Security Controls"); win.geometry("600x500"); win.configure(bg=self.colors['surface']); win.transient(self.window)
        win.update_idletasks(); x = (win.winfo_screenwidth() // 2) - 300; y = (win.winfo_screenheight() // 2) - 250; win.geometry(f"600x500+{x}+{y}")
        header = tk.Frame(win, bg=self.colors['info'], height=60); header.pack(fill=tk.X); header.pack_propagate(False)
        tk.Label(header, text="🖱️ Mouse Button Blocking System", font=("Segoe UI", 14, "bold"), bg=self.colors['info'], fg=self.colors['card']).pack(pady=20)
        content = tk.Frame(win, bg=self.colors['surface']); content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        status_frame = tk.Frame(content, bg=self.colors['card'], pady=15); status_frame.pack(fill=tk.X, pady=(0,20))
        is_active = self.security_manager.mouse_manager.is_active; status_text = "🟢 ACTIVE" if is_active else "🔴 INACTIVE"; status_color = self.colors['success'] if is_active else self.colors['danger']
        tk.Label(status_frame, text=f"Status: {status_text}", font=("Segoe UI", 12, "bold"), bg=self.colors['card'], fg=status_color).pack(pady=10)
        try:
            info = self.security_manager.mouse_manager.get_status(); blocked = info.get('blocked_buttons', [])
            blocked_text = ", ".join(blocked) if isinstance(blocked, list) else str(blocked)
        except Exception:
            blocked_text = "Unavailable"
        tk.Label(status_frame, text=f"Blocked Buttons: {blocked_text}", font=("Segoe UI", 10), bg=self.colors['card'], fg=self.colors['text_primary']).pack(pady=5)
        ctrl = tk.Frame(content, bg=self.colors['card'], pady=20); ctrl.pack(fill=tk.X, pady=(0,20))
        if not is_active:
            tk.Button(ctrl, text="🚀 Activate Mouse Blocking", command=lambda: self._toggle_mouse_and_close(True, win), bg=self.colors['success'], fg=self.colors['card'], font=("Segoe UI", 11, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=10).pack(pady=10)
        else:
            tk.Button(ctrl, text="🛑 Deactivate Mouse Blocking", command=lambda: self._toggle_mouse_and_close(False, win), bg=self.colors['danger'], fg=self.colors['card'], font=("Segoe UI", 11, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=10).pack(pady=10)
        settings = tk.Frame(content, bg=self.colors['card'], pady=15); settings.pack(fill=tk.BOTH, expand=True)
        tk.Label(settings, text="Quick Settings:", font=("Segoe UI", 11, "bold"), bg=self.colors['card'], fg=self.colors['text_primary']).pack(anchor=tk.W, pady=(0,10))
        btns = tk.Frame(settings, bg=self.colors['card']); btns.pack(fill=tk.X, pady=5)
        tk.Button(btns, text="Allow Basic Clicks Only", command=lambda: self._apply_mouse_setting('basic'), bg=self.colors['primary'], fg=self.colors['card'], font=("Segoe UI", 9, "bold"), relief=tk.FLAT, cursor='hand2', padx=15, pady=8).pack(side=tk.LEFT, padx=(0,10))
        tk.Button(btns, text="Block All Buttons", command=lambda: self._apply_mouse_setting('all'), bg=self.colors['warning'], fg=self.colors['card'], font=("Segoe UI", 9, "bold"), relief=tk.FLAT, cursor='hand2', padx=15, pady=8).pack(side=tk.LEFT, padx=(0,10))
        tk.Button(content, text="Close", command=win.destroy, bg=self.colors['secondary'], fg=self.colors['card'], font=("Segoe UI", 10, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=8).pack(pady=20)

    def _toggle_mouse_and_close(self, enable, window):
        try:
            ok = self.security_manager.toggle_mouse_blocking(enable); action = "activated" if enable else "deactivated"
            messagebox.showinfo("✅ Success", f"Mouse blocking {action} successfully!") if ok else messagebox.showerror("❌ Error", f"Failed to {action.replace('ed','')} mouse blocking.")
        finally:
            window.destroy(); self.refresh_status()

    def _apply_mouse_setting(self, t):
        try:
            if t == 'basic': self.security_manager.mouse_manager.allow_basic_clicks(); messagebox.showinfo("✅ Applied", "Mouse set to allow basic clicks only (blocks middle/side buttons)")
            elif t == 'all': self.security_manager.mouse_manager.block_all_buttons(); messagebox.showinfo("✅ Applied", "Mouse set to block all buttons")
        finally:
            self.refresh_status()

    # ===== WINDOW CONTROLS =====
    def show_window_controls(self):
        win = tk.Toplevel(self.window); win.title("🪟 Window Guardian Controls"); win.geometry("600x500"); win.configure(bg=self.colors['surface']); win.transient(self.window)
        win.update_idletasks(); x = (win.winfo_screenwidth() // 2) - 300; y = (win.winfo_screenheight() // 2) - 250; win.geometry(f"600x500+{x}+{y}")
        header = tk.Frame(win, bg=self.colors['primary'], height=60); header.pack(fill=tk.X); header.pack_propagate(False)
        tk.Label(header, text="🪟 Window Protection System", font=("Segoe UI", 14, "bold"), bg=self.colors['primary'], fg=self.colors['card']).pack(pady=20)
        content = tk.Frame(win, bg=self.colors['surface']); content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        status_frame = tk.Frame(content, bg=self.colors['card'], pady=15); status_frame.pack(fill=tk.X, pady=(0,20))
        is_active = self.security_manager.window_manager.is_active; status_text = "🟢 ACTIVE" if is_active else "🔴 INACTIVE"; status_color = self.colors['success'] if is_active else self.colors['danger']
        tk.Label(status_frame, text=f"Status: {status_text}", font=("Segoe UI", 12, "bold"), bg=self.colors['card'], fg=status_color).pack(pady=10)
        try:
            st = self.security_manager.window_manager.get_status(); count = st.get('protected_windows_count', 0); level = st.get('protection_level','Unknown')
        except Exception:
            count = 0; level = 'Unavailable'
        tk.Label(status_frame, text=f"Protected Windows: {count}", font=("Segoe UI", 10), bg=self.colors['card'], fg=self.colors['text_primary']).pack(pady=2)
        tk.Label(status_frame, text=f"Protection Level: {level}", font=("Segoe UI", 10), bg=self.colors['card'], fg=self.colors['text_primary']).pack(pady=2)
        ctrl = tk.Frame(content, bg=self.colors['card'], pady=20); ctrl.pack(fill=tk.X, pady=(0,20))
        if not is_active:
            tk.Button(ctrl, text="🚀 Activate Window Protection", command=lambda: self._toggle_window_and_close(True, win), bg=self.colors['success'], fg=self.colors['card'], font=("Segoe UI", 11, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=10).pack(pady=10)
            info = ("Window Protection will:\n• Disable close and minimize buttons\n• Prevent accidental closes\n• Monitor/guard exam & browser windows")
            tk.Label(ctrl, text=info, font=("Segoe UI", 9), bg=self.colors['card'], fg=self.colors['text_secondary'], justify=tk.LEFT).pack(pady=10)
        else:
            tk.Button(ctrl, text="🛑 Deactivate Window Protection", command=lambda: self._toggle_window_and_close(False, win), bg=self.colors['danger'], fg=self.colors['card'], font=("Segoe UI", 11, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=10).pack(pady=10)
        tk.Button(content, text="Close", command=win.destroy, bg=self.colors['secondary'], fg=self.colors['card'], font=("Segoe UI", 10, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=8).pack(pady=20)

    def _toggle_window_and_close(self, enable, window):
        try:
            ok = self.security_manager.toggle_window_protection(enable); action = "activated" if enable else "deactivated"
            messagebox.showinfo("✅ Success", f"Window protection {action} successfully!") if ok else messagebox.showerror("❌ Error", f"Failed to {action.replace('ed','')} window protection.")
        finally:
            window.destroy(); self.refresh_status()

    # ===== NETWORK CONTROLS =====
    def show_network_controls(self):
        win = tk.Toplevel(self.window); win.title("🌐 Network Security Controls"); win.geometry("500x400"); win.configure(bg=self.colors['surface']); win.transient(self.window)
        win.update_idletasks(); x = (win.winfo_screenwidth() // 2) - 250; y = (win.winfo_screenheight() // 2) - 200; win.geometry(f"500x400+{x}+{y}")
        header = tk.Frame(win, bg=self.colors['warning'], height=60); header.pack(fill=tk.X); header.pack_propagate(False)
        tk.Label(header, text="🌐 Internet Blocking System", font=("Segoe UI", 14, "bold"), bg=self.colors['warning'], fg=self.colors['card']).pack(pady=20)
        content = tk.Frame(win, bg=self.colors['surface']); content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        status = "🟢 BLOCKED" if self.security_manager.network_manager.is_blocked else "🔴 ALLOWED"
        tk.Label(content, text=f"Internet Access: {status}", font=("Segoe UI", 12, "bold"), bg=self.colors['surface'], fg=self.colors['text_primary']).pack(pady=10)
        ctrl = tk.Frame(content, bg=self.colors['card']); ctrl.pack(pady=20, fill=tk.BOTH, expand=True)
        if not self.security_manager.network_manager.is_blocked:
            tk.Button(ctrl, text="🚀 Activate Internet Blocking", command=lambda: [self.toggle_internet_blocking(True), win.destroy()], bg=self.colors['success'], fg=self.colors['card'], font=("Segoe UI", 11, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=10).pack(pady=20)
        else:
            tk.Button(ctrl, text="🛑 Restore Internet Access", command=lambda: [self.toggle_internet_blocking(False), win.destroy()], bg=self.colors['danger'], fg=self.colors['card'], font=("Segoe UI", 11, "bold"), relief=tk.FLAT, cursor='hand2', padx=20, pady=10).pack(pady=20)

    # ===== STATUS & TOGGLES =====
    def refresh_status(self):
        info = self.security_manager.get_system_info() or {}
        if self.security_manager.is_exam_mode:
            self.status_label.config(text="🔒 LOCKDOWN MODE: ACTIVE", fg=self.colors['danger'])
        else:
            self.status_label.config(text="🔓 LOCKDOWN MODE: INACTIVE", fg=self.colors['success'])
        cpu = info.get('cpu_percent', 0.0); mem = info.get('memory_percent', 0.0); procs = info.get('active_processes', 0)
        self.system_info_label.config(text=f"CPU: {cpu:.1f}% | RAM: {mem:.1f}% | Processes: {procs}")
        self.keyboard_status.config(text=("✅ Keyboard" if info.get('hooks_active') else "⚫ Keyboard"), fg=(self.colors['success'] if info.get('hooks_active') else self.colors['text_secondary']))
        self.mouse_status.config(text=("✅ Mouse" if info.get('mouse_blocking') else "⚫ Mouse"), fg=(self.colors['success'] if info.get('mouse_blocking') else self.colors['text_secondary']))
        self.network_status.config(text=("✅ Network" if info.get('internet_blocked') else "⚫ Network"), fg=(self.colors['success'] if info.get('internet_blocked') else self.colors['text_secondary']))
        self.window_status.config(text=("✅ Windows" if info.get('window_protection') else "⚫ Windows"), fg=(self.colors['success'] if info.get('window_protection') else self.colors['text_secondary']))

    def toggle_mouse_blocking(self, enable):
        try:
            return self.security_manager.toggle_mouse_blocking(enable)
        except Exception as e:
            messagebox.showerror("Error", f"Mouse toggle failed: {e}")
            return False

    def toggle_internet_blocking(self, enable):
        try:
            return self.security_manager.toggle_internet_blocking(enable)
        except Exception as e:
            messagebox.showerror("Error", f"Internet toggle failed: {e}")
            return False

    def toggle_window_protection(self, enable):
        try:
            return self.security_manager.toggle_window_protection(enable)
        except Exception as e:
            messagebox.showerror("Error", f"Window toggle failed: {e}")
            return False

    # ===== STOP/EMERGENCY =====
    def stop_exam_mode(self):
        pwd = simpledialog.askstring("🔐 SECURITY VERIFICATION", "Enter admin password to DISABLE lockdown:", show="*")
        if not pwd: return
        import hashlib; h = hashlib.sha256(pwd.encode()).hexdigest()
        if self.db_manager.verify_admin("admin", h):
            self.security_manager.stop_exam_mode(); self.start_btn.config(state=tk.NORMAL); self.stop_btn.config(state=tk.DISABLED); self.refresh_status(); messagebox.showinfo("🔓 LOCKDOWN DISABLED", "All security restrictions have been removed.")
        else:
            messagebox.showerror("❌ ACCESS DENIED", "Invalid admin password!")

    def emergency_stop(self):
        if not messagebox.askyesno("🚨 EMERGENCY STOP", "This is an EMERGENCY STOP procedure.\n\nAre you sure?"): return
        if not messagebox.askyesno("⚠️ FINAL WARNING", "This will IMMEDIATELY disable ALL security.\n\nCONFIRM?"): return
        pwd = simpledialog.askstring("🔐 EMERGENCY AUTH", "Enter admin password for EMERGENCY STOP:", show="*")
        if not pwd: return
        import hashlib; h = hashlib.sha256(pwd.encode()).hexdigest()
        if self.db_manager.verify_admin("admin", h):
            try:
                self.security_manager.stop_exam_mode(); self.start_btn.config(state=tk.NORMAL); self.stop_btn.config(state=tk.DISABLED); self.refresh_status(); messagebox.showwarning("🚨 EMERGENCY STOP EXECUTED", "Emergency stop completed.\nAll security systems disabled.")
            except Exception as e:
                messagebox.showerror("Error", f"Emergency stop failed: {e}")
        else:
            messagebox.showerror("❌ ACCESS DENIED", "Invalid admin password!")

    # ===== AUTO-REFRESH =====
    def start_auto_refresh(self):
        def loop():
            while True:
                try:
                    if self.window.winfo_exists():
                        self.window.after(0, self.refresh_status)
                        threading.Event().wait(2)
                    else:
                        break
                except:
                    break
        threading.Thread(target=loop, daemon=True).start()
=======
            
            logs = self.db_manager.get_activity_logs(20)
            
            for log in logs:
                action, details, timestamp, blocked = log
                status = "🚫 BLOCKED" if blocked else "✅ ALLOWED"
                
                if blocked or "SUSPICIOUS" in action or "TERMINATED" in action:
                    severity = "🔴 HIGH"
                elif "BLOCKED" in action or "SECURITY" in action:
                    severity = "🟡 MED"
                else:
                    severity = "🟢 LOW"
                
                try:
                    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                    time_str = dt.strftime("%H:%M:%S")
                except:
                    time_str = timestamp
                
                self.activity_tree.insert("", 0, values=(time_str, severity, action, details or "No details", status))
        except Exception as e:
            pass

    def on_close(self):
        result = messagebox.askyesno("⚠️ Confirm Exit",
                                    "Close Admin Panel?\n\nThe system will continue running in the background.\n"
                                    "Access it again from the system tray.")
        if result:
            self.window.withdraw()

    def show(self):
        self.window.deiconify()
        self.window.lift()
        self.refresh_status()
        self.load_blocked_keys()
        self.load_blocked_mouse_buttons()
        self.load_blocked_websites()
>>>>>>> 8516873 (Initial commit: Project version 1)
=======
        # Show basic error dialog
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Startup Error", f"Failed to start application:\\n\\n{str(e)}")
        root.destroy()
>>>>>>> de2d156 (Initial commit)
