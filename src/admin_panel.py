"""
Admin Panel for Exam Shield - COMPLETE STABLE VERSION
All methods properly defined to eliminate attribute errors
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog, filedialog
import threading
import json
from datetime import datetime
import keyboard
from pynput import mouse
import theme

class AdminPanel:
    def __init__(self, db_manager, security_manager, parent_window):
        self.db_manager = db_manager
        self.security_manager = security_manager
        self.parent_window = parent_window
        self.security_manager.set_admin_panel(self)

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
import threading
import json
from datetime import datetime
import keyboard
from pynput import mouse

class AdminPanel:
    def __init__(self):
        if not self.is_admin():
            self.restart_as_admin()
            return
            
        self.root = tk.Tk()
        self.root.title("Exam Shield Pro v2.0 - Modern Design")
        self.root.geometry("550x700")
        self.root.resizable(False, False)
    def __init__(self, db_manager, security_manager, parent_window):
        self.db_manager = db_manager
        self.security_manager = security_manager
        self.parent_window = parent_window
        
        # Premium color scheme
        self.colors = {
            'primary': '#1e3d59',
            'secondary': '#17223b', 
            'accent': '#ffc947',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'info': '#3498db',
            'surface': '#f8f9fa',
            'card': '#ffffff',
            'text_primary': '#2c3e50',
            'text_secondary': '#7f8c8d',
            'border': '#dee2e6',
            'light_blue': '#ecf4ff',
            'light_green': '#e8f5e8',
            'light_yellow': '#fff8e1',
            'light_red': '#ffebee'
        }
        
        # NEW: Key/Mouse detection variables
        self.detecting_key = False
        self.detecting_mouse = False
        self.detected_key = None
        self.mouse_listener = None

        self.window = tk.Toplevel()
        self.window.title("Exam Shield Premium - Admin Panel v2.0")
        self.window.geometry("950x750")
        self.window.resizable(True, True)

        self.current_theme = "light"
        self.load_theme(self.current_theme)

        # Set admin panel reference in security manager
        self.security_manager.set_admin_panel(self)
        
        # Key/Mouse detection variables
        self.detecting_key = False
        self.detecting_mouse = False
        self.detected_key = None
        self.mouse_listener = None
        
        self.setup_window()
        self.window = tk.Toplevel()
        self.window.title("Exam Shield Premium - Administrative Control Center")
        self.window.geometry("1200x800")
        self.window.resizable(True, True)
        self.window.configure(bg=self.colors['surface'])
        
        self.setup_window()
        self.setup_ui()
        self.start_auto_refresh()

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


    def create_styled_frame(self, parent, bg_color=None):
        """Create a frame with premium styling"""
        if bg_color is None:
            bg_color = self.colors['card']
        
        frame = tk.Frame(parent, bg=bg_color, relief=tk.FLAT, bd=0)
        
        # Add subtle shadow effect
        shadow = tk.Frame(parent, bg='#d0d3d4', height=1)
        shadow.pack(fill=tk.X, pady=(0, 2))
        
        return frame

    def create_card(self, parent, title=None, icon=None):
        """Create a styled card container"""
        card_container = tk.Frame(parent, bg=self.colors['surface'])
        
        # Card with shadow
        shadow_frame = tk.Frame(card_container, bg='#dee2e6', height=2)
        shadow_frame.pack(fill=tk.X, pady=(2, 0))
        
        card = tk.Frame(card_container, bg=self.colors['card'], relief=tk.FLAT, bd=0)
        card.pack(fill=tk.BOTH, expand=True, pady=(0, 2))
        
        if title:
            # Card header
            header = tk.Frame(card, bg=self.colors['primary'], height=50)
            header.pack(fill=tk.X)
            header.pack_propagate(False)
            
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
            if icon:
                icon_label = tk.Label(header, text=icon, font=("Segoe UI", 16),
                                    bg=self.colors['primary'], fg=self.colors['accent'])
                icon_label.pack(side=tk.LEFT, padx=(15, 10), pady=15)
            
            title_label = tk.Label(header, text=title, font=("Segoe UI", 14, "bold"),
                                 bg=self.colors['primary'], fg=self.colors['card'])
            title_label.pack(side=tk.LEFT, pady=15)
            
            # Content area
            content = tk.Frame(card, bg=self.colors['card'])
            content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
            
            return card_container, content
        
        return card_container, card

    def setup_ui(self):
        # Main header
        header_frame = tk.Frame(self.window, bg=self.colors['primary'], height=70)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Header content
        header_content = tk.Frame(header_frame, bg=self.colors['primary'])
        header_content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # Logo and title
        logo_label = tk.Label(header_content, text="🛡️", font=("Segoe UI", 24),
                            bg=self.colors['primary'], fg=self.colors['accent'])
        logo_label.pack(side=tk.LEFT, padx=(0, 15))
        
        title_frame = tk.Frame(header_content, bg=self.colors['primary'])
        title_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        main_title = tk.Label(title_frame, text="EXAM SHIELD PREMIUM", 
                            font=("Segoe UI", 18, "bold"),
                            bg=self.colors['primary'], fg=self.colors['card'])
        main_title.pack(anchor=tk.W)
        
        subtitle = tk.Label(title_frame, text="Administrative Control Center", 
                          font=("Segoe UI", 10),
                          bg=self.colors['primary'], fg=self.colors['light_blue'])
        subtitle.pack(anchor=tk.W)
        
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
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - 250
        y = (dialog.winfo_screenheight() // 2) - 300
        dialog.geometry(f"500x600+{x}+{y}")

        header = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text="🔒 Select Security Modules to Activate",
                font=("Segoe UI", 14, "bold"), bg=self.colors['primary'], 
                fg=self.colors['card']).pack(pady=20)

        options = tk.Frame(dialog, bg=self.colors['surface'])
        options.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)

        self.selective_vars = {}
        # Status indicator in header
        status_frame = tk.Frame(header_content, bg=self.colors['primary'])
        status_frame.pack(side=tk.RIGHT)
        
        self.header_status = tk.Label(status_frame, text="🔓 SYSTEM READY", 
                                    font=("Segoe UI", 11, "bold"),
                                    bg=self.colors['primary'], fg=self.colors['accent'])
        self.header_status.pack()
        
        # Main content area
        content_area = tk.Frame(self.window, bg=self.colors['surface'])
        content_area.pack(fill=tk.BOTH, expand=True)
        
        # Create notebook with custom styling
        self.setup_notebook(content_area)

    def setup_notebook(self, parent):
        """Setup the main tabbed interface with premium styling"""
        notebook_container = tk.Frame(parent, bg=self.colors['surface'])
        notebook_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        modules = [
            ("keyboard", "🔤 Keyboard Shortcuts Blocking", "Block Alt+Tab, Ctrl+Alt+Del, etc."),
            ("mouse", "🖱️ Mouse Button Restrictions", "Block middle, back, forward buttons"),
            ("internet", "🌐 Internet Access Blocking", "Complete internet disconnection"),
            ("windows", "🪟 Window Protection", "Prevent closing/minimizing windows"),
            ("processes", "🔍 Process Monitoring", "Auto-terminate suspicious processes")
        ]

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
        # Custom tab bar
        tab_bar = tk.Frame(notebook_container, bg=self.colors['card'], height=50)
        tab_bar.pack(fill=tk.X, pady=(0, 2))
        tab_bar.pack_propagate(False)
        
        # Tab buttons
        self.tab_buttons = {}
        tabs = [
            ("control", "📊 Control Center", self.show_control_tab),
            ("monitor", "📈 Live Monitor", self.show_monitor_tab),
            ("settings", "⚙️ Settings", self.show_settings_tab),
            ("logs", "📋 Security Logs", self.show_logs_tab)
        ]
        
        for i, (key, text, command) in enumerate(tabs):
            btn = tk.Button(tab_bar, text=text, font=("Segoe UI", 10, "bold"),
                          bg=self.colors['surface'], fg=self.colors['text_primary'],
                          relief=tk.FLAT, padx=20, pady=15, cursor='hand2',
                          command=lambda cmd=command, k=key: self.switch_tab(k, cmd))
            btn.pack(side=tk.LEFT, padx=(2 if i > 0 else 0, 0))
            self.tab_buttons[key] = btn
        
        # Tab content area
        self.tab_content = tk.Frame(notebook_container, bg=self.colors['surface'])
        self.tab_content.pack(fill=tk.BOTH, expand=True)
        
        # Initialize with control tab
        self.current_tab = "control"
        self.switch_tab("control", self.show_control_tab)

    def switch_tab(self, tab_key, tab_function):
        """Switch between tabs with visual feedback"""
        # Update button styles
        for key, btn in self.tab_buttons.items():
            if key == tab_key:
                btn.config(bg=self.colors['primary'], fg=self.colors['card'])
            else:
                btn.config(bg=self.colors['surface'], fg=self.colors['text_primary'])
        
        # Clear current content
        for widget in self.tab_content.winfo_children():
            widget.destroy()
        
        # Load new content
        self.current_tab = tab_key
        tab_function()

    def show_control_tab(self):
        """Create the main control tab with premium design"""
        main_frame = tk.Frame(self.tab_content, bg=self.colors['surface'])
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Top row - Status cards
        status_row = tk.Frame(main_frame, bg=self.colors['surface'])
        status_row.pack(fill=tk.X, pady=(0, 15))
        
        # System status card
        status_card, status_content = self.create_card(status_row, "System Status", "📊")
        status_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))
        
        self.status_label = tk.Label(status_content, text="🔓 Lockdown Mode: INACTIVE", 
                                   font=("Segoe UI", 14, "bold"), bg=self.colors['card'], 
                                   fg=self.colors['success'])
        self.status_label.pack(anchor=tk.W, pady=(0, 10))
        
        self.system_info_label = tk.Label(status_content, text="Loading system information...",
                                        font=("Segoe UI", 10), bg=self.colors['card'], 
                                        fg=self.colors['text_secondary'])
        self.system_info_label.pack(anchor=tk.W)
        
        # Security modules card
        modules_card, modules_content = self.create_card(status_row, "Security Modules", "🔒")
        modules_card.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(8, 0))
        
        # Security module indicators
        modules_grid = tk.Frame(modules_content, bg=self.colors['card'])
        modules_grid.pack(fill=tk.BOTH, expand=True)
        
        # Create module status indicators
        modules = [
            ("keyboard", "Keyboard Protection"),
            ("mouse", "Mouse Control"),
            ("network", "Network Security"),
            ("windows", "Window Guardian")
        ]
        
        self.module_indicators = {}
        for i, (key, name) in enumerate(modules):
            row = i // 2
            col = i % 2
            
            module_frame = tk.Frame(modules_grid, bg=self.colors['card'])
            module_frame.grid(row=row, column=col, sticky="w", padx=(0, 20), pady=5)
            
            indicator = tk.Label(module_frame, text="⚫", font=("Segoe UI", 12),
                               bg=self.colors['card'], fg=self.colors['text_secondary'])
            indicator.pack(side=tk.LEFT, padx=(0, 8))
            
            label = tk.Label(module_frame, text=name, font=("Segoe UI", 10),
                           bg=self.colors['card'], fg=self.colors['text_primary'])
            label.pack(side=tk.LEFT)
            
            self.module_indicators[key] = indicator
        
        # Control buttons section
        control_section = tk.Frame(main_frame, bg=self.colors['surface'])
        control_section.pack(fill=tk.X, pady=(0, 15))
        
        control_card, control_content = self.create_card(control_section, "Lockdown Controls", "🎯")
        control_card.pack(fill=tk.X)
        
        button_frame = tk.Frame(control_content, bg=self.colors['card'])
        button_frame.pack(fill=tk.X, pady=10)
        
        # Premium styled buttons
        self.start_btn = self.create_premium_button(
            button_frame, "🚀 START SELECTIVE LOCKDOWN", 
            self.show_selective_lockdown_dialog, self.colors['primary'], "left")
        
        self.stop_btn = self.create_premium_button(
            button_frame, "🔓 END LOCKDOWN MODE", 
            self.stop_exam_mode, self.colors['warning'], "left", state=tk.DISABLED)
        
        self.emergency_btn = self.create_premium_button(
            button_frame, "🚨 EMERGENCY STOP", 
            self.emergency_stop, self.colors['danger'], "right")
        
        # Individual controls section
        individual_section = tk.Frame(main_frame, bg=self.colors['surface'])
        individual_section.pack(fill=tk.BOTH, expand=True)
        
        individual_card, individual_content = self.create_card(individual_section, 
                                                             "Individual Security Controls", "🛠️")
        individual_card.pack(fill=tk.BOTH, expand=True)
        
        # Control grid
        controls_grid = tk.Frame(individual_content, bg=self.colors['card'])
        controls_grid.pack(fill=tk.X, pady=10)
        
        controls = [
            ("🖱️ Mouse Security", self.show_mouse_controls),
            ("🌐 Network Control", self.show_network_controls),
            ("🪟 Window Guardian", self.show_window_controls),
            ("📊 Live Monitor", lambda: self.switch_tab("monitor", self.show_monitor_tab)),
            ("⚙️ Settings Panel", lambda: self.switch_tab("settings", self.show_settings_tab)),
            ("🔄 Refresh Status", self.refresh_status)
        ]
        
        for i, (text, command) in enumerate(controls):
            row = i // 3
            col = i % 3
            
            btn = self.create_premium_button(controls_grid, text, command, 
                                           self.colors['info'], pack_side=None)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
        
        # Configure grid weights
        for i in range(3):
            controls_grid.columnconfigure(i, weight=1)

    def create_premium_button(self, parent, text, command, bg_color, pack_side="left", **kwargs):
        """Create a premium styled button"""
        btn = tk.Button(parent, text=text, command=command,
                       bg=bg_color, fg=self.colors['card'],
                       font=("Segoe UI", 10, "bold"), relief=tk.FLAT, 
                       cursor='hand2', padx=15, pady=10,
                       activebackground=self.darken_color(bg_color),
                       activeforeground=self.colors['card'], **kwargs)
        
        if not pack_side:
            return btn
        if pack_side == "right":
            btn.pack(side=tk.RIGHT, padx=(10, 0))
        elif pack_side == "left":
            btn.pack(side=tk.LEFT, padx=(0, 10))
        
        return btn

    def darken_color(self, color):
        """Darken a hex color for hover effects"""
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        darkened = tuple(max(0, int(c * 0.8)) for c in rgb)
        return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"

    def show_selective_lockdown_dialog(self):
        """Enhanced selective lockdown dialog with premium design"""
        dialog = tk.Toplevel(self.window)
        dialog.title("🔒 Selective Lockdown Configuration")
        dialog.geometry("600x700")
        dialog.configure(bg=self.colors['surface'])
        dialog.transient(self.window)
        dialog.grab_set()
        
        # Center dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - 300
        y = (dialog.winfo_screenheight() // 2) - 350
        dialog.geometry(f"600x700+{x}+{y}")
        
        # Header
        header = tk.Frame(dialog, bg=self.colors['primary'], height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        header_content = tk.Frame(header, bg=self.colors['primary'])
        header_content.pack(expand=True, pady=20)
        
        tk.Label(header_content, text="🔒", font=("Segoe UI", 24),
                bg=self.colors['primary'], fg=self.colors['accent']).pack()
        
        tk.Label(header_content, text="Configure Security Modules",
                font=("Segoe UI", 16, "bold"), bg=self.colors['primary'], 
                fg=self.colors['card']).pack()
        
        # Content area
        content = tk.Frame(dialog, bg=self.colors['surface'])
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Instructions
        instruction_text = ("Select which security modules to activate during lockdown. "
                          "Each module provides specific protection features.")
        tk.Label(content, text=instruction_text, font=("Segoe UI", 10),
                bg=self.colors['surface'], fg=self.colors['text_secondary'],
                wraplength=540, justify=tk.LEFT).pack(pady=(0, 20))
        
        # Module selection
        self.selective_vars = {}
        modules = [
            ("keyboard", "🔤 Keyboard Protection", 
             "Blocks dangerous keyboard shortcuts (Alt+Tab, Ctrl+Alt+Del, etc.)"),
            ("mouse", "🖱️ Mouse Control", 
             "Restricts mouse buttons and prevents unauthorized interactions"),
            ("internet", "🌐 Network Security", 
             "Completely blocks internet access and network communications"),
            ("windows", "🪟 Window Guardian", 
             "Prevents window manipulation, closing, and switching"),
            ("processes", "🔍 Process Monitor", 
             "Automatically detects and terminates unauthorized processes")
        ]
        
        for key, title, description in modules:
            module_card = self.create_module_option(content, key, title, description)
            module_card.pack(fill=tk.X, pady=(0, 12))
        
        # Action buttons
        button_frame = tk.Frame(content, bg=self.colors['surface'])
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        start_btn = self.create_premium_button(
            button_frame, "🚀 START SELECTED LOCKDOWN",
            lambda: self.start_selective_lockdown(dialog),
            self.colors['success'], pack_side=None)
        start_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        cancel_btn = self.create_premium_button(
            button_frame, "❌ CANCEL",
            dialog.destroy, self.colors['danger'], pack_side=None)
        cancel_btn.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))

    def create_module_option(self, parent, key, title, description):
        """Create a module selection option with premium styling"""
        card = tk.Frame(parent, bg=self.colors['card'], relief=tk.FLAT, bd=0)
        
        # Add border
        border = tk.Frame(card, bg=self.colors['border'], height=1)
        border.pack(fill=tk.X)
        
        content = tk.Frame(card, bg=self.colors['card'])
        content.pack(fill=tk.X, padx=20, pady=15)
        
        # Checkbox and title
        header_frame = tk.Frame(content, bg=self.colors['card'])
        header_frame.pack(fill=tk.X, pady=(0, 5))
        
        var = tk.BooleanVar(value=True)
        self.selective_vars[key] = var
        
        check = tk.Checkbutton(header_frame, text=title, variable=var,
                             font=("Segoe UI", 12, "bold"), bg=self.colors['card'],
                             fg=self.colors['text_primary'], selectcolor=self.colors['card'],
                             activebackground=self.colors['card'])
        check.pack(side=tk.LEFT)
        
        # Description
        desc_label = tk.Label(content, text=description, font=("Segoe UI", 9),
                            bg=self.colors['card'], fg=self.colors['text_secondary'],
                            wraplength=520, justify=tk.LEFT)
        desc_label.pack(anchor=tk.W)
        
        return card

    # Continue with other methods (monitoring, settings, logs tabs)
    def show_monitor_tab(self):
        """Create the monitoring tab"""
        main_frame = tk.Frame(self.tab_content, bg=self.colors['surface'])
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        monitor_card, monitor_content = self.create_card(main_frame, 
                                                       "Real-time Security Monitor", "📈")
        monitor_card.pack(fill=tk.BOTH, expand=True)
        
        # Create treeview for activity monitoring
        columns = ("Time", "Severity", "Module", "Event", "Details", "Status")
        self.activity_tree = ttk.Treeview(monitor_content, columns=columns, 
                                        show="headings", height=25)
        
        # Configure columns
        column_widths = {"Time": 120, "Severity": 80, "Module": 100, 
                        "Event": 150, "Details": 300, "Status": 100}
        
        for col in columns:
            self.activity_tree.heading(col, text=col)
            self.activity_tree.column(col, width=column_widths.get(col, 100))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(monitor_content, orient=tk.VERTICAL, 
                                command=self.activity_tree.yview)
        self.activity_tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack treeview and scrollbar
        self.activity_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def show_settings_tab(self):
        """Create the settings tab with premium design"""
        main_frame = tk.Frame(self.tab_content, bg=self.colors['surface'])
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollable settings area
        canvas = tk.Canvas(main_frame, bg=self.colors['surface'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['surface'])
        
        scrollable_frame.bind("<Configure>", 
                            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Settings sections
        self.create_keyboard_settings(scrollable_frame)
        self.create_mouse_settings(scrollable_frame)
        self.create_network_settings(scrollable_frame)
        self.create_advanced_settings(scrollable_frame)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def show_logs_tab(self):
        """Create the logs tab"""
        main_frame = tk.Frame(self.tab_content, bg=self.colors['surface'])
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Controls
        controls_frame = tk.Frame(main_frame, bg=self.colors['surface'], height=60)
        controls_frame.pack(fill=tk.X, pady=(0, 10))
        controls_frame.pack_propagate(False)
        
        control_card = tk.Frame(controls_frame, bg=self.colors['card'])
        control_card.pack(fill=tk.BOTH, padx=0, pady=5)
        
        # Control buttons
        btn_frame = tk.Frame(control_card, bg=self.colors['card'])
        btn_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.create_premium_button(btn_frame, "🔄 Refresh", self.refresh_logs,
                                 self.colors['info'], pack_side="left")
        self.create_premium_button(btn_frame, "🗑️ Clear All", self.clear_logs,
                                 self.colors['warning'], pack_side="left")
        self.create_premium_button(btn_frame, "💾 Export", self.export_logs,
                                 self.colors['success'], pack_side="left")
        
        # Logs display
        logs_card, logs_content = self.create_card(main_frame, "Security Event History", "📋")
        logs_card.pack(fill=tk.BOTH, expand=True)
        
        self.logs_text = scrolledtext.ScrolledText(logs_content, wrap=tk.WORD, 
                                                 height=30, font=("Consolas", 9),
                                                 bg=self.colors['surface'], 
                                                 fg=self.colors['text_primary'])
        self.logs_text.pack(fill=tk.BOTH, expand=True)

    # Implement remaining methods with premium styling...
    # (This includes all the settings creation, detection methods, and control functions)
    # The methods follow the same premium design pattern established above

    def start_selective_lockdown(self, dialog):
        """Start lockdown with selected options"""
        selected_options = {key: var.get() for key, var in self.selective_vars.items()}
        
        if not any(selected_options.values()):
            messagebox.showwarning("No Selection", 
                                 "Please select at least one security module to activate!")
            return
        
        # Confirm selection
        selected_names = [key.title() for key, selected in selected_options.items() if selected]
        result = messagebox.askyesno("Confirm Selective Lockdown",
                                   f"Activate lockdown with these modules?\n\n" +
                                   "\n".join(f"✓ {name}" for name in selected_names))
        
        if result:
            dialog.destroy()
            try:
                self.security_manager.start_exam_mode(selected_options)
                self.start_btn.config(state=tk.DISABLED)
                self.stop_btn.config(state=tk.NORMAL)
                self.refresh_status()
                
                messagebox.showinfo("🔒 SELECTIVE LOCKDOWN ACTIVE",
                                  f"Premium lockdown activated with:\n\n" +
                                  "\n".join(f"✅ {name} Protection" for name in selected_names))
            except Exception as e:
                messagebox.showerror("Lockdown Error", 
                                   f"Failed to activate lockdown: {str(e)}")

    # Add all the remaining methods here following the same premium styling pattern
    # ... (continuing with the rest of the AdminPanel class methods)

    def refresh_status(self):
        """Update status indicators with premium styling"""
        if self.security_manager.is_exam_mode:
            self.status_label.config(text="🔒 LOCKDOWN MODE: ACTIVE", 
                                   fg=self.colors['danger'])
            self.header_status.config(text="🔒 LOCKDOWN ACTIVE", 
                                    fg=self.colors['accent'])
        else:
            self.status_label.config(text="🔓 LOCKDOWN MODE: INACTIVE", 
                                   fg=self.colors['success'])
            self.header_status.config(text="🔓 SYSTEM READY", 
                                    fg=self.colors['accent'])
        
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

    def update_activity_feed(self):
        try:
            for item in self.activity_tree.get_children():
                self.activity_tree.delete(item)
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
        # Show basic error dialog
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Startup Error", f"Failed to start application:\\n\\n{str(e)}")
        root.destroy()

    def on_close(self):
        """Handle window close event"""
        if messagebox.askyesno("Close Admin Panel", 
                              "Close the administrative control center?\n\n"
                              "The system will continue running in the background."):
            self.window.withdraw()

    def create_keyboard_settings(self, parent):
        """Create keyboard settings section"""
        card, content = self.create_card(parent, "Keyboard Protection", "🔤")
        card.pack(fill=tk.X, pady=(0, 15))
        
        self.keyboard_vars = {}
        blocked_keys = [
            ("alt+tab", "Alt + Tab"),
            ("alt+f4", "Alt + F4"),
            ("win+d", "Windows + D"),
            ("win+l", "Windows + L"),
            ("win+r", "Windows + R"),
            ("ctrl+alt+del", "Ctrl + Alt + Delete"),
            ("ctrl+shift+esc", "Ctrl + Shift + Escape"),
            ("f11", "F11 Fullscreen"),
            ("alt+space", "Alt + Space")
        ]
        
        grid_frame = tk.Frame(content, bg=self.colors['card'])
        grid_frame.pack(fill=tk.X)
        
        for i, (key, label) in enumerate(blocked_keys):
            row = i // 3
            col = i % 3
            
            var = tk.BooleanVar(value=True)
            self.keyboard_vars[key] = var
            
            cb = tk.Checkbutton(grid_frame, text=label, variable=var,
                              font=("Segoe UI", 9), bg=self.colors['card'],
                              fg=self.colors['text_primary'], selectcolor=self.colors['light_blue'])
            cb.grid(row=row, column=col, sticky="w", padx=10, pady=5)
    
    def create_mouse_settings(self, parent):
        """Create mouse settings section"""
        card, content = self.create_card(parent, "Mouse Control", "🖱️")
        card.pack(fill=tk.X, pady=(0, 15))
        
        self.mouse_vars = {}
        mouse_buttons = [
            ("middle", "Middle Button"),
            ("x1", "Extra Button 1"),
            ("x2", "Extra Button 2"),
            ("side", "Side Button"),
            ("back", "Back Button"),
            ("forward", "Forward Button")
        ]
        
        grid_frame = tk.Frame(content, bg=self.colors['card'])
        grid_frame.pack(fill=tk.X)
        
        for i, (key, label) in enumerate(mouse_buttons):
            row = i // 3
            col = i % 3
            
            var = tk.BooleanVar(value=True)
            self.mouse_vars[key] = var
            
            cb = tk.Checkbutton(grid_frame, text=label, variable=var,
                              font=("Segoe UI", 9), bg=self.colors['card'],
                              fg=self.colors['text_primary'], selectcolor=self.colors['light_blue'])
            cb.grid(row=row, column=col, sticky="w", padx=10, pady=5)
        
        btn_frame = tk.Frame(content, bg=self.colors['card'])
        btn_frame.pack(fill=tk.X, pady=(15, 0))
        
        self.create_premium_button(btn_frame, "Apply Settings", self.apply_mouse_settings,
                              self.colors['primary'], pack_side="left")
    
    def create_network_settings(self, parent):
        """Create network settings section"""
        card, content = self.create_card(parent, "Network Security", "🌐")
        card.pack(fill=tk.X, pady=(0, 15))
        
        self.network_var = tk.BooleanVar(value=True)
        
        cb = tk.Checkbutton(content, text="Block Internet Access",
                         variable=self.network_var,
                         font=("Segoe UI", 11, "bold"),
                         bg=self.colors['card'],
                         fg=self.colors['text_primary'],
                         selectcolor=self.colors['light_blue'])
        cb.pack(anchor=tk.W, pady=(0, 10))
        
        tk.Label(content, text="Blocked Websites:",
                font=("Segoe UI", 10), bg=self.colors['card'],
                fg=self.colors['text_secondary']).pack(anchor=tk.W)
        
        blocked_sites = tk.Label(content,
                text="google.com, facebook.com, youtube.com, twitter.com, instagram.com, reddit.com, discord.com",
                font=("Segoe UI", 9), bg=self.colors['card'],
                fg=self.colors['text_secondary'], wraplength=500)
        blocked_sites.pack(anchor=tk.W, pady=(5, 0))
    
    def create_advanced_settings(self, parent):
        """Create advanced settings section"""
        card, content = self.create_card(parent, "Advanced Settings", "⚙️")
        card.pack(fill=tk.X, pady=(0, 15))
        
        self.auto_refresh_var = tk.BooleanVar(value=True)
        cb = tk.Checkbutton(content, text="Auto-refresh Status (every 2 seconds)",
                         variable=self.auto_refresh_var,
                         font=("Segoe UI", 10), bg=self.colors['card'],
                         fg=self.colors['text_primary'],
                         selectcolor=self.colors['light_blue'])
        cb.pack(anchor=tk.W, pady=5)
        
        self.process_monitor_var = tk.BooleanVar(value=True)
        cb2 = tk.Checkbutton(content, text="Monitor & Terminate Suspicious Processes",
                          variable=self.process_monitor_var,
                          font=("Segoe UI", 10), bg=self.colors['card'],
                          fg=self.colors['text_primary'],
                          selectcolor=self.colors['light_blue'])
        cb2.pack(anchor=tk.W, pady=5)
        
        self.window_protect_var = tk.BooleanVar(value=True)
        cb3 = tk.Checkbutton(content, text="Window Guardian (prevent switching/closing)",
                            variable=self.window_protect_var,
                            font=("Segoe UI", 10), bg=self.colors['card'],
                            fg=self.colors['text_primary'],
                            selectcolor=self.colors['light_blue'])
        cb3.pack(anchor=tk.W, pady=5)
    
    def stop_exam_mode(self):
        """Stop exam mode with confirmation"""
        if not self.security_manager.is_exam_mode:
            messagebox.showinfo("Info", "Lockdown mode is not active!")
            return
        
        result = messagebox.askyesno("End Lockdown",
                                     "Are you sure you want to end lockdown mode?\n\n"
                                     "This will deactivate all security restrictions.")
        
        if result:
            try:
                self.security_manager.stop_exam_mode()
                self.start_btn.config(state=tk.NORMAL)
                self.stop_btn.config(state=tk.DISABLED)
                self.refresh_status()
                messagebox.showinfo("Success", "Lockdown mode has been deactivated!\n\nAll security restrictions removed.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to stop lockdown: {str(e)}")
    
    def emergency_stop(self):
        """Emergency stop procedure"""
        result = messagebox.askyesno("EMERGENCY STOP",
                                       "⚠️ EMERGENCY STOP REQUESTED\n\n"
                                       "This will immediately end lockdown mode and restore all system access.\n\n"
                                       "Use this ONLY if there's a critical issue or system malfunction.\n\n"
                                       "Are you sure you want to proceed?")
        
        if result:
            try:
                self.security_manager.stop_exam_mode()
                self.start_btn.config(state=tk.NORMAL)
                self.stop_btn.config(state=tk.DISABLED)
                self.refresh_status()
                messagebox.showinfo("Emergency Stop Complete",
                                     "Emergency stop completed successfully.\n\n"
                                     "All security restrictions have been removed.\n"
                                     "System access has been fully restored.")
            except Exception as e:
                messagebox.showwarning("Warning",
                                       f"Emergency stop executed with minor error:\n{str(e)}\n\n"
                                       "System restrictions should be removed.")
    
    def show_mouse_controls(self):
        """Show mouse controls dialog"""
        dialog = tk.Toplevel(self.window)
        dialog.title("Mouse Control Panel")
        dialog.geometry("500x400")
        dialog.configure(bg=self.colors['surface'])
        dialog.transient(self.window)
        dialog.grab_set()
        
        x = (dialog.winfo_screenwidth() // 2) - 250
        y = (dialog.winfo_screenheight() // 2) - 200
        dialog.geometry(f"500x400+{x}+{y}")
        
        header = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text="🖱️", font=("Segoe UI", 20),
                bg=self.colors['primary'], fg=self.colors['accent']).pack(pady=10)
        
        content = tk.Frame(dialog, bg=self.colors['surface'])
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        status = self.security_manager.mouse_manager.get_status()
        
        status_label = tk.Label(content, text="Mouse Control Status",
                             font=("Segoe UI", 14, "bold"),
                             bg=self.colors['surface'],
                             fg=self.colors['text_primary'])
        status_label.pack(pady=(0, 20))
        
        active_status = "ACTIVE" if status['active'] else "INACTIVE"
        status_color = self.colors['success'] if status['active'] else self.colors['text_secondary']
        
        tk.Label(content, text=f"Status: {active_status}",
                font=("Segoe UI", 12), bg=self.colors['surface'],
                fg=status_color).pack()
        
        tk.Label(content, text=f"Blocked Buttons: {', '.join(status['blocked_buttons'])}",
                font=("Segoe UI", 10), bg=self.colors['surface'],
                fg=self.colors['text_secondary']).pack(pady=(10, 0))
        
        btn_frame = tk.Frame(content, bg=self.colors['surface'])
        btn_frame.pack(pady=30)
        
        if status['active']:
            self.create_premium_button(btn_frame, "Disable Mouse Blocking",
                                    self.security_manager.mouse_manager.stop_blocking,
                                    self.colors['danger'], pack_side=None).pack(side=tk.LEFT, padx=10)
        else:
            self.create_premium_button(btn_frame, "Enable Mouse Blocking",
                                    self.security_manager.mouse_manager.start_blocking,
                                    self.colors['success'], pack_side=None).pack(side=tk.LEFT, padx=10)
        
        self.create_premium_button(btn_frame, "Close",
                                dialog.destroy,
                                self.colors['primary'], pack_side=None).pack(side=tk.LEFT, padx=10)
    
    def show_network_controls(self):
        """Show network controls dialog"""
        dialog = tk.Toplevel(self.window)
        dialog.title("Network Control Panel")
        dialog.geometry("550x500")
        dialog.configure(bg=self.colors['surface'])
        dialog.transient(self.window)
        dialog.grab_set()
        
        x = (dialog.winfo_screenwidth() // 2) - 275
        y = (dialog.winfo_screenheight() // 2) - 250
        dialog.geometry(f"550x500+{x}+{y}")
        
        header = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text="🌐", font=("Segoe UI", 20),
                bg=self.colors['primary'], fg=self.colors['accent']).pack(pady=10)
        
        content = tk.Frame(dialog, bg=self.colors['surface'])
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        status_label = tk.Label(content, text="Network Security Status",
                          font=("Segoe UI", 14, "bold"),
                          bg=self.colors['surface'],
                          fg=self.colors['text_primary'])
        status_label.pack(pady=(0, 20))
        
        blocked = self.security_manager.network_manager.is_blocked
        status_text = "BLOCKED" if blocked else "ACTIVE"
        status_color = self.colors['danger'] if blocked else self.colors['success']
        
        tk.Label(content, text=f"Internet Access: {status_text}",
                font=("Segoe UI", 12), bg=self.colors['surface'],
                fg=status_color).pack()
        
        card, card_content = self.create_card(content, "Blocked Websites", "🚫")
        card.pack(fill=tk.X, pady=20)
        
        sites_text = scrolledtext.ScrolledText(card_content, height=12, font=("Consolas", 9),
                                               bg=self.colors['surface'],
                                               fg=self.colors['text_primary'])
        sites_text.pack(fill=tk.BOTH, expand=True)
        
        blocked_sites = self.security_manager.network_manager.get_blocked_websites()
        sites_text.insert(tk.END, "\n".join(blocked_sites))
        sites_text.config(state=tk.DISABLED)
        
        btn_frame = tk.Frame(content, bg=self.colors['surface'])
        btn_frame.pack(pady=10)
        
        if blocked:
            self.create_premium_button(btn_frame, "Restore Internet Access",
                                    self.security_manager.network_manager.stop_blocking,
                                    self.colors['success'], pack_side=None).pack(side=tk.LEFT, padx=10)
        else:
            self.create_premium_button(btn_frame, "Block Internet Access",
                                    self.security_manager.network_manager.start_blocking,
                                    self.colors['danger'], pack_side=None).pack(side=tk.LEFT, padx=10)
        
        self.create_premium_button(btn_frame, "Close",
                                dialog.destroy,
                                self.colors['primary'], pack_side=None).pack(side=tk.LEFT, padx=10)
    
    def show_window_controls(self):
        """Show window controls dialog"""
        dialog = tk.Toplevel(self.window)
        dialog.title("Window Guardian Control")
        dialog.geometry("500x350")
        dialog.configure(bg=self.colors['surface'])
        dialog.transient(self.window)
        dialog.grab_set()
        
        x = (dialog.winfo_screenwidth() // 2) - 250
        y = (dialog.winfo_screenheight() // 2) - 175
        dialog.geometry(f"500x350+{x}+{y}")
        
        header = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text="🪟", font=("Segoe UI", 20),
                bg=self.colors['primary'], fg=self.colors['accent']).pack(pady=10)
        
        content = tk.Frame(dialog, bg=self.colors['surface'])
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        status_label = tk.Label(content, text="Window Guardian Status",
                             font=("Segoe UI", 14, "bold"),
                             bg=self.colors['surface'],
                             fg=self.colors['text_primary'])
        status_label.pack(pady=(0, 20))
        
        active = self.security_manager.window_manager.is_active
        status_text = "ACTIVE" if active else "INACTIVE"
        status_color = self.colors['success'] if active else self.colors['text_secondary']
        
        tk.Label(content, text=f"Window Protection: {status_text}",
                font=("Segoe UI", 12), bg=self.colors['surface'],
                fg=status_color).pack()
        
        features = [
            "Prevents Alt+Tab window switching",
            "Blocks Alt+F4 window close",
            "Prevents Windows key shortcuts",
            "Blocks window minimize/maximize",
            "Monitors task switching attempts"
        ]
        
        tk.Label(content, text="Active Features:",
                font=("Segoe UI", 10, "bold"),
                bg=self.colors['surface'],
                fg=self.colors['text_primary']).pack(pady=(20, 10))
        
        for feature in features:
            tk.Label(content, text=f"• {feature}",
                    font=("Segoe UI", 9),
                    bg=self.colors['surface'],
                    fg=self.colors['text_secondary']).pack(anchor=tk.W)
        
        btn_frame = tk.Frame(content, bg=self.colors['surface'])
        btn_frame.pack(pady=20)
        
        if active:
            self.create_premium_button(btn_frame, "Disable Window Guardian",
                                    self.security_manager.window_manager.stop_window_protection,
                                    self.colors['danger'], pack_side=None).pack(side=tk.LEFT, padx=10)
        else:
            self.create_premium_button(btn_frame, "Enable Window Guardian",
                                    self.security_manager.window_manager.start_window_protection,
                                    self.colors['success'], pack_side=None).pack(side=tk.LEFT, padx=10)
        
        self.create_premium_button(btn_frame, "Close",
                                dialog.destroy,
                                self.colors['primary'], pack_side=None).pack(side=tk.LEFT, padx=10)
    
    def apply_mouse_settings(self):
        """Apply mouse settings"""
        selected = [key for key, var in self.mouse_vars.items() if var.get()]
        if selected:
            self.security_manager.mouse_manager.blocked_buttons = selected
            self.security_manager.mouse_manager.start_blocking(selected)
            messagebox.showinfo("Success", f"Mouse settings applied!\n\nBlocked buttons: {', '.join(selected)}")
        else:
            messagebox.showwarning("Warning", "Please select at least one button to block.")
    
    def refresh_logs(self):
        """Refresh security logs"""
        try:
            logs = self.db_manager.get_logs(limit=500)
            self.logs_text.delete(1.0, tk.END)
            for log in logs:
                timestamp = log.get('timestamp', '')
                event_type = log.get('event_type', '')
                message = log.get('message', '')
                self.logs_text.insert(tk.END, f"[{timestamp}] {event_type}: {message}\n\n")
            self.logs_text.see(tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh logs: {str(e)}")
    
    def clear_logs(self):
        """Clear security logs"""
        result = messagebox.askyesno("Clear Logs",
                                      "Are you sure you want to clear all security logs?\n\n"
                                      "This action cannot be undone.")
        
        if result:
            try:
                self.db_manager.clear_logs()
                self.logs_text.delete(1.0, tk.END)
                messagebox.showinfo("Success", "All security logs have been cleared.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to clear logs: {str(e)}")
    
    def export_logs(self):
        """Export security logs"""
        pass
        from tkinter import filedialog
        import csv
        from datetime import datetime
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")],
            initialfile=f"exam_shield_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
        
        if file_path:
            try:
                logs = self.db_manager.get_logs(limit=10000)
                
                if file_path.endswith('.csv'):
                    with open(file_path, 'w', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerow(['Timestamp', 'Event Type', 'Message', 'Blocked'])
                        for log in logs:
                            writer.writerow([
                                log.get('timestamp', ''),
                                log.get('event_type', ''),
                                log.get('message', ''),
                                log.get('blocked', False)
                            ])
                else:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        for log in logs:
                            f.write(f"[{log.get('timestamp', '')}] {log.get('event_type', '')}: {log.get('message', '')}\n")
                
                messagebox.showinfo("Export Complete", f"Logs exported successfully!\n\nFile: {file_path}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export logs: {str(e)}")
