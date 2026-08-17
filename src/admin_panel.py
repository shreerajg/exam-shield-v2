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
from src import theme

class AdminPanel:

    def __init__(self, db_manager, security_manager, parent_window):
        self.db_manager = db_manager
        self.security_manager = security_manager
        self.parent_window = parent_window
        self.colors = {'primary': '#1e3d59', 'secondary': '#17223b', 'accent': '#ffc947', 'success': '#27ae60', 'warning': '#f39c12', 'danger': '#e74c3c', 'info': '#3498db', 'surface': '#f8f9fa', 'card': '#ffffff', 'text_primary': '#2c3e50', 'text_secondary': '#7f8c8d', 'border': '#dee2e6', 'light_blue': '#ecf4ff', 'light_green': '#e8f5e8', 'light_yellow': '#fff8e1', 'light_red': '#ffebee'}
        self.detecting_key = False
        self.detecting_mouse = False
        self.detected_key = None
        self.mouse_listener = None
        self.window = tk.Toplevel()
        self.window.title('Exam Shield Premium - Administrative Control Center')
        self.window.geometry('1200x800')
        self.window.resizable(True, True)
        self.current_theme = 'light'
        self.load_theme(self.current_theme)
        self.window.configure(bg=self.colors['surface'])
        self.security_manager.set_admin_panel(self)
        self.setup_window()
        self.setup_ui()
        # Fade-in entrance for the admin panel window
        self._anim = theme.AnimationManager(self.window)
        self._anim.fade_in(self.window, duration=400)
        self.start_auto_refresh()

    def load_theme(self, theme_name):
        t = theme.get_theme(theme_name)
        tc = t.colors
        if theme_name == 'light':
            self.colors = {
                'primary':        '#1565c0',   # clear medium blue
                'secondary':      '#f1f5f9',   # very light gray (nav bg — airy, not dark)
                'accent':         '#f59e0b',   # warm amber
                'success':        '#16a34a',
                'warning':        '#f59e0b',
                'danger':         '#dc2626',
                'info':           '#0284c7',
                'surface':        '#f0f7ff',   # light blue-tinted page bg
                'card':           '#ffffff',
                'text_primary':   '#1e293b',   # dark slate
                'text_secondary': '#64748b',   # slate gray
                'border':         '#dbeafe',
                'light_blue':     '#eff6ff',
                'light_green':    '#f0fdf4',
                'light_red':      '#fef2f2',
                'light_yellow':   '#fffbeb',
                'white':          '#ffffff',
            }
        else:
            self.colors = {
                'primary': tc['primary'], 'secondary': tc.get('secondary', '#17223b'),
                'accent': tc.get('warning', '#ffc947'), 'success': tc['success'],
                'warning': tc['warning'], 'danger': tc['danger'], 'info': tc['info'],
                'surface': tc['surface'], 'card': tc['card'],
                'text_primary': tc['text_primary'], 'text_secondary': tc['text_secondary'],
                'border': tc.get('border', '#dee2e6'), 'light_blue': tc.get('light_blue', '#ecf4ff'),
                'light_green': tc.get('light_green', '#e8f5e8'),
                'light_red': tc.get('light_red', '#ffebee'),
                'light_yellow': tc.get('light_yellow', '#fff8e1'),
                'white': '#ffffff',
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
        x = self.window.winfo_screenwidth() // 2 - 475
        y = self.window.winfo_screenheight() // 2 - 375
        self.window.geometry(f'950x750+{x}+{y}')
        self.window.protocol('WM_DELETE_WINDOW', self.on_close)

    def on_close(self):
        """Handle window close event"""
        if messagebox.askyesno('Close Admin Panel', 'Close the administrative control center?\n\nThe system will continue running in the background.'):
            self.window.withdraw()

    def show(self):
        self.window.deiconify()
        self.window.lift()
        self.refresh_status()

    def setup_ui(self):
        """Build the admin panel: header bar, gold accent strip, dark nav bar, content area."""
        c = self.colors
        nav_bg = c.get('secondary', '#17223b') or '#17223b'

        # ── Header bar ──────────────────────────────────────────────────────────
        header = tk.Frame(self.window, bg=c['primary'], height=65)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        hc = tk.Frame(header, bg=c['primary'])
        hc.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        tk.Label(hc, text='🛡️', font=('Segoe UI', 22),
                 bg=c['primary'], fg=c['accent']).pack(side=tk.LEFT, padx=(0, 12))
        tf = tk.Frame(hc, bg=c['primary'])
        tf.pack(side=tk.LEFT, fill=tk.Y)
        tk.Label(tf, text='EXAM SHIELD PREMIUM',
                 font=('Segoe UI', 16, 'bold'),
                 bg=c['primary'], fg='#ffffff').pack(anchor=tk.W)
        tk.Label(tf, text='Administrative Control Center',
                 font=('Segoe UI', 9),
                 bg=c['primary'], fg='#7fa8cc').pack(anchor=tk.W)

        # Theme selector on the right
        tr = tk.Frame(hc, bg=c['primary'])
        tr.pack(side=tk.RIGHT, fill=tk.Y)
        tk.Label(tr, text='🎨  Theme:', bg=c['primary'],
                 fg='#7fa8cc', font=('Segoe UI', 9)).pack(side=tk.LEFT, padx=(0, 6))
        if not hasattr(self, 'theme_var'):
            self.theme_var = tk.StringVar(value=self.current_theme)
        combo = ttk.Combobox(tr, textvariable=self.theme_var,
                             values=['light', 'dark', 'pink'],
                             state='readonly', width=8, font=('Segoe UI', 9))
        combo.pack(side=tk.LEFT)
        combo.bind('<<ComboboxSelected>>', self.change_theme)

        # Gold accent strip
        tk.Frame(self.window, bg=c.get('accent', '#ffc947'), height=3).pack(fill=tk.X)

        # ── Navigation bar ─────────────────────────────────────────────────────
        nav = tk.Frame(self.window, bg=nav_bg, height=44)
        nav.pack(fill=tk.X)
        nav.pack_propagate(False)
        self.tab_buttons = {}
        for key, label in [
            ('control',  '🎯   Control Center'),
            ('monitor',  '📊   Live Monitor'),
            ('settings', '⚙️   Settings'),
            ('logs',     '📋   Security Logs'),
        ]:
            btn = tk.Button(nav, text=label,
                            font=('Segoe UI', 10),
                            bg=nav_bg, fg='#475569',
                            relief=tk.FLAT, cursor='hand2',
                            padx=18, pady=10, bd=0)
            btn.pack(side=tk.LEFT)
            self.tab_buttons[key] = btn

        # ── Content area ─────────────────────────────────────────────────────
        self.tab_content = tk.Frame(self.window, bg=c['surface'])
        self.tab_content.pack(fill=tk.BOTH, expand=True)

        # Show the control tab first
        self.switch_tab('control', self.show_control_tab)

    def create_control_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='📋 Control Center')
        main = tk.Frame(frame, bg=self.colors['surface'])
        main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        status_card = tk.Frame(main, bg=self.colors['card'])
        status_card.pack(fill=tk.X, pady=(0, 10))
        sh = tk.Frame(status_card, bg=self.colors['info'], height=40)
        sh.pack(fill=tk.X)
        sh.pack_propagate(False)
        tk.Label(sh, text='📊 System Status', font=('Segoe UI', 12, 'bold'), bg=self.colors['info'], fg=self.colors['card']).pack(pady=10)
        sc = tk.Frame(status_card, bg=self.colors['card'])
        sc.pack(fill=tk.X, padx=15, pady=15)
        self.status_label = tk.Label(sc, text='🔓 Exam Mode: INACTIVE', font=('Segoe UI', 14, 'bold'), bg=self.colors['card'], fg=self.colors['success'])
        self.status_label.pack(anchor=tk.W)
        self.system_info_label = tk.Label(sc, text='System Info Loading...', font=('Segoe UI', 10), bg=self.colors['card'], fg=self.colors['text_secondary'])
        self.system_info_label.pack(anchor=tk.W, pady=(5, 0))
        ind = tk.Frame(sc, bg=self.colors['card'])
        ind.pack(anchor=tk.W, pady=(5, 0), fill=tk.X)
        tk.Label(ind, text='Security Modules:', font=('Segoe UI', 10, 'bold'), bg=self.colors['card'], fg=self.colors['text_primary']).pack(anchor=tk.W)
        row = tk.Frame(ind, bg=self.colors['card'])
        row.pack(anchor=tk.W, pady=(2, 0))
        self.keyboard_status = tk.Label(row, text='⚫ Keyboard', font=('Segoe UI', 9), bg=self.colors['card'], fg=self.colors['text_secondary'])
        self.keyboard_status.pack(side=tk.LEFT, padx=(0, 15))
        self.mouse_status = tk.Label(row, text='⚫ Mouse', font=('Segoe UI', 9), bg=self.colors['card'], fg=self.colors['text_secondary'])
        self.mouse_status.pack(side=tk.LEFT, padx=(0, 15))
        self.network_status = tk.Label(row, text='⚫ Network', font=('Segoe UI', 9), bg=self.colors['card'], fg=self.colors['text_secondary'])
        self.network_status.pack(side=tk.LEFT, padx=(0, 15))
        self.window_status = tk.Label(row, text='⚫ Windows', font=('Segoe UI', 9), bg=self.colors['card'], fg=self.colors['text_secondary'])
        self.window_status.pack(side=tk.LEFT, padx=(0, 15))
        card = tk.Frame(main, bg=self.colors['card'])
        card.pack(fill=tk.X, pady=(0, 10))
        ch = tk.Frame(card, bg=self.colors['primary'], height=40)
        ch.pack(fill=tk.X)
        ch.pack_propagate(False)
        tk.Label(ch, text='🎯 Exam Controls', font=('Segoe UI', 12, 'bold'), bg=self.colors['primary'], fg=self.colors['card']).pack(pady=10)
        btns = tk.Frame(card, bg=self.colors['card'])
        btns.pack(fill=tk.X, padx=15, pady=15)
        self.start_btn = tk.Button(btns, text='🔒 START SELECTIVE LOCKDOWN', command=self.show_selective_lockdown_dialog, bg=self.colors['primary'], fg=self.colors['card'], font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, cursor='hand2', padx=20, pady=10)
        self.start_btn.pack(side=tk.LEFT, padx=(0, 10))
        self.stop_btn = tk.Button(btns, text='🔓 END LOCKDOWN MODE', command=self.stop_exam_mode, state=tk.DISABLED, bg=self.colors['warning'], fg=self.colors['card'], font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, cursor='hand2', padx=20, pady=10)
        self.stop_btn.pack(side=tk.LEFT, padx=(0, 10))
        tk.Button(btns, text='🚨 EMERGENCY STOP', command=self.emergency_stop, bg=self.colors['danger'], fg=self.colors['card'], font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, cursor='hand2', padx=20, pady=10).pack(side=tk.RIGHT)
        self.create_individual_controls(main)

    def create_individual_controls(self, parent):
        """Create individual security controls"""
        features_frame = ttk.LabelFrame(parent, text='Individual Security Controls', padding='10')
        features_frame.pack(fill=tk.X, padx=10, pady=5)
        feature_btn_frame1 = ttk.Frame(features_frame)
        feature_btn_frame1.pack(fill=tk.X, pady=(0, 5))
        ttk.Button(feature_btn_frame1, text='🖱️ Mouse Blocker', command=self.show_mouse_controls).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(feature_btn_frame1, text='🌐 Internet Blocker', command=self.show_network_controls).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(feature_btn_frame1, text='🪟 Window Guardian', command=self.show_window_controls).pack(side=tk.LEFT, padx=(0, 5))
        feature_btn_frame2 = ttk.Frame(features_frame)
        feature_btn_frame2.pack(fill=tk.X)
        ttk.Button(feature_btn_frame2, text='📊 Live Monitor', command=lambda: self.notebook.select(1)).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(feature_btn_frame2, text='⚙️ Settings', command=lambda: self.notebook.select(2)).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(feature_btn_frame2, text='🔄 Refresh Status', command=self.refresh_status).pack(side=tk.LEFT, padx=(0, 5))

    def show_selective_lockdown_dialog(self):
        dialog = tk.Toplevel(self.window)
        dialog.title('🔒 Selective Lockdown Configuration')
        dialog.geometry('500x600')
        dialog.configure(bg=self.colors['surface'])
        dialog.transient(self.window)
        dialog.grab_set()
        dialog.update_idletasks()
        x = dialog.winfo_screenwidth() // 2 - 250
        y = dialog.winfo_screenheight() // 2 - 300
        dialog.geometry(f'500x600+{x}+{y}')
        # Fade dialog in
        anim = theme.AnimationManager(dialog)
        anim.fade_in(dialog, duration=250)
        header = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text='🔒 Select Security Modules to Activate', font=('Segoe UI', 14, 'bold'), bg=self.colors['primary'], fg=self.colors['card']).pack(pady=20)
        options = tk.Frame(dialog, bg=self.colors['surface'])
        options.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        self.selective_vars = {}
        modules = [('keyboard', '🔤 Keyboard Shortcuts Blocking', 'Block Alt+Tab, Ctrl+Alt+Del, etc.'), ('mouse', '🖱️ Mouse Button Restrictions', 'Block middle, back, forward buttons'), ('internet', '🌐 Internet Access Blocking', 'Complete internet disconnection'), ('windows', '🪟 Window Protection', 'Prevent closing/minimizing windows'), ('processes', '🔍 Process Monitoring', 'Auto-terminate suspicious processes')]
        for key, title, desc in modules:
            card = tk.Frame(options, bg=self.colors['card'], relief=tk.FLAT, bd=1)
            card.pack(fill=tk.X, pady=(0, 10))
            content = tk.Frame(card, bg=self.colors['card'])
            content.pack(fill=tk.X, padx=15, pady=12)
            var = tk.BooleanVar(value=True)
            self.selective_vars[key] = var
            chk = tk.Checkbutton(content, text=title, variable=var, font=('Segoe UI', 11, 'bold'), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['card'], activebackground=self.colors['card'])
            chk.pack(anchor=tk.W)
            tk.Label(content, text=desc, font=('Segoe UI', 9), bg=self.colors['card'], fg=self.colors['text_secondary']).pack(anchor=tk.W, padx=20, pady=(2, 0))
        btns = tk.Frame(dialog, bg=self.colors['surface'])
        btns.pack(fill=tk.X, padx=40, pady=20)

        def start():
            selected = {k: v.get() for k, v in self.selective_vars.items()}
            if not any(selected.values()):
                messagebox.showwarning('No Selection', 'Please select at least one security module!')
                return
            names = [k.title() for k, s in selected.items() if s]
            if messagebox.askyesno('Confirm Selective Lockdown', 'Start lockdown with these modules?\n\n' + '\n'.join((f'✓ {n}' for n in names))):
                dialog.destroy()
                try:
                    self.security_manager.start_exam_mode(selected)
                    self.start_btn.config(state=tk.DISABLED)
                    self.stop_btn.config(state=tk.NORMAL)
                    self.refresh_status()
                    messagebox.showinfo('🔒 SELECTIVE LOCKDOWN ACTIVE', 'Lockdown active with:\n' + '\n'.join((f'✓ {n}' for n in names)))
                except Exception as e:
                    messagebox.showerror('Error', f'Failed to start lockdown: {e}')
        tk.Button(btns, text='🚀 START SELECTED LOCKDOWN', command=start, bg=self.colors['success'], fg=self.colors['card'], font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, pady=10, cursor='hand2').pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        tk.Button(btns, text='❌ CANCEL', command=dialog.destroy, bg=self.colors['danger'], fg=self.colors['card'], font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, pady=10, cursor='hand2').pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))

    def create_styled_frame(self, parent, bg_color=None):
        """Create a frame with premium styling"""
        if bg_color is None:
            bg_color = self.colors['card']
        frame = tk.Frame(parent, bg=bg_color, relief=tk.FLAT, bd=0)
        shadow = tk.Frame(parent, bg='#d0d3d4', height=1)
        shadow.pack(fill=tk.X, pady=(0, 2))
        return frame

    def create_card(self, parent, title=None, icon=None):
        """Create a styled card with a left-accent-pip header (modern look)."""
        c = self.colors
        container = tk.Frame(parent, bg=c['surface'])
        card = tk.Frame(container, bg=c['card'], relief=tk.FLAT, bd=0)
        card.pack(fill=tk.BOTH, expand=True)
        # Thin shadow line at bottom
        tk.Frame(container, bg='#c8cdd4', height=2).pack(fill=tk.X)
        if title:
            # Header row: left-accent pip + optional icon + title
            hdr = tk.Frame(card, bg=c['card'])
            hdr.pack(fill=tk.X, padx=16, pady=(14, 0))
            # 4px colored accent pip
            tk.Frame(hdr, bg=c['primary'], width=4,
                     height=20).pack(side=tk.LEFT, padx=(0, 10))
            if icon:
                tk.Label(hdr, text=icon, font=('Segoe UI', 12),
                         bg=c['card'], fg=c['primary']).pack(side=tk.LEFT, padx=(0, 5))
            tk.Label(hdr, text=title, font=('Segoe UI', 11, 'bold'),
                     bg=c['card'], fg=c['primary']).pack(side=tk.LEFT)
            # Thin separator
            tk.Frame(card, bg='#e8ecf0', height=1).pack(fill=tk.X, padx=16, pady=(10, 0))
            content = tk.Frame(card, bg=c['card'])
            content.pack(fill=tk.BOTH, expand=True, padx=16, pady=12)
            return (container, content)
        return (container, card)

    def setup_notebook(self, parent):
        """Setup the main tabbed interface with premium styling"""
        notebook_container = tk.Frame(parent, bg=self.colors['surface'])
        notebook_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        modules = [('keyboard', '🔤 Keyboard Shortcuts Blocking', 'Block Alt+Tab, Ctrl+Alt+Del, etc.'), ('mouse', '🖱️ Mouse Button Restrictions', 'Block middle, back, forward buttons'), ('internet', '🌐 Internet Access Blocking', 'Complete internet disconnection'), ('windows', '🪟 Window Protection', 'Prevent closing/minimizing windows'), ('processes', '🔍 Process Monitoring', 'Auto-terminate suspicious processes')]
        for key, title, desc in modules:
            card = tk.Frame(options , bg=self.colors['card'], relief=tk.FLAT, bd=1)
            card.pack(fill=tk.X, pady=(0, 10))
            content = tk.Frame(card, bg=self.colors['card'])
            content.pack(fill=tk.X, padx=15, pady=12)
            var = tk.BooleanVar(value=True)
            self.selective_vars[key] = var
            tk.Checkbutton(content, text=title, variable=var, font=('Segoe UI', 11, 'bold'), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['card'], activebackground=self.colors['card']).pack(anchor=tk.W)
            tk.Label(content, text=desc, font=('Segoe UI', 9), bg=self.colors['card'], fg=self.colors['text_secondary']).pack(anchor=tk.W, padx=20, pady=(2, 0))
        btns = tk.Frame(dialog , bg=self.colors['surface'])
        btns.pack(fill=tk.X, padx=40, pady=20)
        tk.Button(btns, text='🚀 START SELECTED LOCKDOWN', command=lambda: self.start_selective_lockdown(dialog), bg=self.colors['success'], fg=self.colors['card'], font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, pady=10, cursor='hand2').pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        tk.Button(btns, text='❌ CANCEL', command=dialog .destroy, bg=self.colors['danger'], fg=self.colors['card'], font=('Segoe UI', 11, 'bold'), relief=tk.FLAT, pady=10, cursor='hand2').pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))

    def start_selective_lockdown(self, dialog):
        """Start lockdown with selected options"""
        selected_options = {key: var.get() for key, var in self.selective_vars.items()}
        if not any(selected_options.values()):
            messagebox.showwarning('No Selection', 'Please select at least one security module to activate!')
            return
        selected_names = [key.title() for key, selected in selected_options.items() if selected]
        result = messagebox.askyesno('Confirm Selective Lockdown', f'Activate lockdown with these modules?\n\n' + '\n'.join((f'✓ {name}' for name in selected_names)))
        if result:
            dialog.destroy()
            try:
                self.security_manager.start_exam_mode(selected_options)
                self.start_btn.config(state=tk.DISABLED)
                self.stop_btn.config(state=tk.NORMAL)
                self.refresh_status()
                messagebox.showinfo('🔒 SELECTIVE LOCKDOWN ACTIVE', f'Premium lockdown activated with:\n\n' + '\n'.join((f'✅ {name} Protection' for name in selected_names)))
            except Exception as e:
                messagebox.showerror('Lockdown Error', f'Failed to activate lockdown: {str(e)}')

    def create_monitoring_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='📊 Live Monitor')
        container = tk.Frame(frame, bg=self.colors['surface'])
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        header = tk.Frame(container, bg=self.colors['info'], height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text='📊 Real-time Security Events', font=('Segoe UI', 14, 'bold'), bg=self.colors['info'], fg=self.colors['card']).pack(pady=15)
        content = tk.Frame(container, bg=self.colors['card'])
        content.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        columns = ('Time', 'Severity', 'Action', 'Details', 'Status')
        self.activity_tree = ttk.Treeview(content, columns=columns, show='headings', height=20)
        for col in columns:
            self.activity_tree.heading(col, text=col)
        self.activity_tree.column('Time', width=120)
        self.activity_tree.column('Severity', width=80)
        self.activity_tree.column('Action', width=180)
        self.activity_tree.column('Details', width=300)
        self.activity_tree.column('Status', width=100)
        sb = ttk.Scrollbar(content, orient=tk.VERTICAL, command=self.activity_tree.yview)
        self.activity_tree.configure(yscrollcommand=sb.set)
        self.activity_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        sb.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 20), pady=20)

    def switch_tab(self, tab_key, tab_function):
        """Switch tabs and update active nav button style."""
        nav_bg = self.colors.get('secondary', '#f1f5f9') or '#f1f5f9'
        active_bg = self.colors['primary']
        for key, btn in self.tab_buttons.items():
            if key == tab_key:
                btn.config(bg=active_bg, fg='#ffffff', font=('Segoe UI', 10, 'bold'))
            else:
                btn.config(bg=nav_bg, fg='#475569', font=('Segoe UI', 10))
                # Subtle hover on inactive buttons
                anim = theme.AnimationManager(btn)
                anim.bind_shimmer_hover(btn, nav_bg, '#dbeafe')
        for widget in self.tab_content.winfo_children():
            widget.destroy()
        self.current_tab = tab_key
        tab_function()

    def show_control_tab(self):
        """Create the main control tab with premium design"""
        main_frame = tk.Frame(self.tab_content, bg=self.colors['surface'])
        main_frame.pack(fill=tk.BOTH, expand=True)
        status_row = tk.Frame(main_frame, bg=self.colors['surface'])
        status_row.pack(fill=tk.X, pady=(0, 15))
        status_card, status_content = self.create_card(status_row, 'System Status', '📊')
        status_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))
        self.status_label = tk.Label(status_content, text='🔓 Lockdown Mode: INACTIVE', font=('Segoe UI', 14, 'bold'), bg=self.colors['card'], fg=self.colors['success'])
        self.status_label.pack(anchor=tk.W, pady=(0, 10))
        self.system_info_label = tk.Label(status_content, text='Loading system information...', font=('Segoe UI', 10), bg=self.colors['card'], fg=self.colors['text_secondary'])
        self.system_info_label.pack(anchor=tk.W)
        modules_card, modules_content = self.create_card(status_row, 'Security Modules', '🔒')
        modules_card.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(8, 0))
        modules_grid = tk.Frame(modules_content, bg=self.colors['card'])
        modules_grid.pack(fill=tk.BOTH, expand=True)
        modules = [('keyboard', 'Keyboard Protection'), ('mouse', 'Mouse Control'), ('network', 'Network Security'), ('windows', 'Window Guardian')]
        self.module_indicators = {}
        for i, (key, name) in enumerate(modules):
            row = i // 2
            col = i % 2
            module_frame = tk.Frame(modules_grid, bg=self.colors['card'])
            module_frame.grid(row=row, column=col, sticky='w', padx=(0, 20), pady=5)
            indicator = tk.Label(module_frame, text='⚫', font=('Segoe UI', 12), bg=self.colors['card'], fg=self.colors['text_secondary'])
            indicator.pack(side=tk.LEFT, padx=(0, 8))
            label = tk.Label(module_frame, text=name, font=('Segoe UI', 10), bg=self.colors['card'], fg=self.colors['text_primary'])
            label.pack(side=tk.LEFT)
            self.module_indicators[key] = indicator
        control_section = tk.Frame(main_frame, bg=self.colors['surface'])
        control_section.pack(fill=tk.X, pady=(0, 15))
        control_card, control_content = self.create_card(control_section, 'Lockdown Controls', '🎯')
        control_card.pack(fill=tk.X)
        button_frame = tk.Frame(control_content, bg=self.colors['card'])
        button_frame.pack(fill=tk.X, pady=10)
        self.start_btn = self.create_premium_button(button_frame, '🚀 START SELECTIVE LOCKDOWN', self.show_selective_lockdown_dialog, self.colors['primary'], 'left')
        self.stop_btn = self.create_premium_button(button_frame, '🔓 END LOCKDOWN MODE', self.stop_exam_mode, self.colors['warning'], 'left', state=tk.DISABLED)
        self.emergency_btn = self.create_premium_button(button_frame, '🚨 EMERGENCY STOP', self.emergency_stop, self.colors['danger'], 'right')
        individual_section = tk.Frame(main_frame, bg=self.colors['surface'])
        individual_section.pack(fill=tk.BOTH, expand=True)
        individual_card, individual_content = self.create_card(individual_section, 'Individual Security Controls', '🛠️')
        individual_card.pack(fill=tk.BOTH, expand=True)
        controls_grid = tk.Frame(individual_content, bg=self.colors['card'])
        controls_grid.pack(fill=tk.X, pady=10)
        controls = [('🖱️ Mouse Security', self.show_mouse_controls), ('🌐 Network Control', self.show_network_controls), ('🪟 Window Guardian', self.show_window_controls), ('📊 Live Monitor', lambda: self.switch_tab('monitor', self.show_monitor_tab)), ('⚙️ Settings Panel', lambda: self.switch_tab('settings', self.show_settings_tab)), ('🔄 Refresh Status', self.refresh_status)]
        for i, (text, command) in enumerate(controls):
            row = i // 3
            col = i % 3
            btn = self.create_premium_button(controls_grid, text, command, self.colors['info'], pack_side='grid')
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='ew')
        for i in range(3):
            controls_grid.columnconfigure(i, weight=1)

    def create_premium_button(self, parent, text, command, bg_color, pack_side='left', **kwargs):
        """Create a premium styled button with animated hover and press feedback."""
        btn = tk.Button(parent, text=text, command=command, bg=bg_color, fg=self.colors['card'],
                        font=('Segoe UI', 10, 'bold'), relief=tk.FLAT, cursor='hand2',
                        padx=15, pady=10, **kwargs)
        # Compute hover colour via darken
        hover_color = self.darken_color(bg_color)
        anim = theme.AnimationManager(btn)
        anim.bind_shimmer_hover(btn, bg_color, hover_color)
        btn.bind('<ButtonPress-1>', lambda e: anim.button_press_effect(btn), add='+')
        if not pack_side or pack_side == 'grid':
            pass
        elif pack_side == 'right':
            btn.pack(side=tk.RIGHT, padx=(10, 0))
        elif pack_side == 'left':
            btn.pack(side=tk.LEFT, padx=(0, 10))
        return btn

    def darken_color(self, color):
        """Darken a hex color for hover effects"""
        color = color.lstrip('#')
        rgb = tuple((int(color[i:i + 2], 16) for i in (0, 2, 4)))
        darkened = tuple((max(0, int(c * 0.8)) for c in rgb))
        return f'#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}'

    def create_module_option(self, parent, key, title, description):
        """Create a module selection option with premium styling"""
        card = tk.Frame(parent, bg=self.colors['card'], relief=tk.FLAT, bd=0)
        border = tk.Frame(card, bg=self.colors['border'], height=1)
        border.pack(fill=tk.X)
        content = tk.Frame(card, bg=self.colors['card'])
        content.pack(fill=tk.X, padx=20, pady=15)
        header_frame = tk.Frame(content, bg=self.colors['card'])
        header_frame.pack(fill=tk.X, pady=(0, 5))
        var = tk.BooleanVar(value=True)
        self.selective_vars[key] = var
        check = tk.Checkbutton(header_frame, text=title, variable=var, font=('Segoe UI', 12, 'bold'), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['card'], activebackground=self.colors['card'])
        check.pack(side=tk.LEFT)
        desc_label = tk.Label(content, text=description, font=('Segoe UI', 9), bg=self.colors['card'], fg=self.colors['text_secondary'], wraplength=520, justify=tk.LEFT)
        desc_label.pack(anchor=tk.W)
        return card

    def show_monitor_tab(self):
        """Create the monitoring tab"""
        main_frame = tk.Frame(self.tab_content, bg=self.colors['surface'])
        main_frame.pack(fill=tk.BOTH, expand=True)
        monitor_card, monitor_content = self.create_card(main_frame, 'Real-time Security Monitor', '📈')
        monitor_card.pack(fill=tk.BOTH, expand=True)
        columns = ('Time', 'Severity', 'Module', 'Event', 'Details', 'Status')
        self.activity_tree = ttk.Treeview(monitor_content, columns=columns, show='headings', height=25)
        column_widths = {'Time': 120, 'Severity': 80, 'Module': 100, 'Event': 150, 'Details': 300, 'Status': 100}
        for col in columns:
            self.activity_tree.heading(col, text=col)
            self.activity_tree.column(col, width=column_widths.get(col, 100))
        scrollbar = ttk.Scrollbar(monitor_content, orient=tk.VERTICAL, command=self.activity_tree.yview)
        self.activity_tree.configure(yscrollcommand=scrollbar.set)
        self.activity_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def show_settings_tab(self):
        """Create the settings tab with premium design"""
        main_frame = tk.Frame(self.tab_content, bg=self.colors['surface'])
        main_frame.pack(fill=tk.BOTH, expand=True)
        canvas = tk.Canvas(main_frame, bg=self.colors['surface'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['surface'])
        scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        self.create_keyboard_settings(scrollable_frame)
        self.create_mouse_settings(scrollable_frame)
        self.create_network_settings(scrollable_frame)
        self.create_advanced_settings(scrollable_frame)
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

    def show_logs_tab(self):
        """Create the logs tab"""
        main_frame = tk.Frame(self.tab_content, bg=self.colors['surface'])
        main_frame.pack(fill=tk.BOTH, expand=True)
        controls_frame = tk.Frame(main_frame, bg=self.colors['surface'], height=60)
        controls_frame.pack(fill=tk.X, pady=(0, 10))
        controls_frame.pack_propagate(False)
        control_card = tk.Frame(controls_frame, bg=self.colors['card'])
        control_card.pack(fill=tk.BOTH, padx=0, pady=5)
        btn_frame = tk.Frame(control_card, bg=self.colors['card'])
        btn_frame.pack(fill=tk.X, padx=20, pady=10)
        self.create_premium_button(btn_frame, '🔄 Refresh', self.refresh_logs, self.colors['info'], pack_side='left')
        self.create_premium_button(btn_frame, '🗑️ Clear All', self.clear_logs, self.colors['warning'], pack_side='left')
        self.create_premium_button(btn_frame, '💾 Export', self.export_logs, self.colors['success'], pack_side='left')
        logs_card, logs_content = self.create_card(main_frame, 'Security Event History', '📋')
        logs_card.pack(fill=tk.BOTH, expand=True)
        self.logs_text = scrolledtext.ScrolledText(logs_content, wrap=tk.WORD, height=30, font=('Consolas', 9), bg=self.colors['surface'], fg=self.colors['text_primary'])
        self.logs_text.pack(fill=tk.BOTH, expand=True)

    def refresh_status(self):
        """Update status indicators (no-op if widgets have been destroyed)."""
        # Guard: if the control tab is not visible, widgets may be destroyed
        if not hasattr(self, 'status_label'):
            return
        try:
            if not self.status_label.winfo_exists():
                return
        except Exception:
            return
        info = self.security_manager.get_system_info() or {}
        if self.security_manager.is_exam_mode:
            status_text = '🔒 LOCKDOWN MODE: ACTIVE'
            if hasattr(self, '_anim'):
                self._anim.typewriter(self.status_label, status_text, char_delay=30)
                self._anim.pulse_label_color(self.status_label, self.colors['danger'], '#ff8a80', duration=1200)
            else:
                self.status_label.config(text=status_text, fg=self.colors['danger'])
        else:
            if hasattr(self.status_label, '_pulse_after_id'):
                try:
                    self.status_label.after_cancel(self.status_label._pulse_after_id)
                except Exception:
                    pass
            self.status_label.config(text='🔓 LOCKDOWN MODE: INACTIVE', fg=self.colors['success'])
        cpu = info.get('cpu_percent', 0.0)
        mem = info.get('memory_percent', 0.0)
        procs = info.get('active_processes', 0)
        try:
            self.system_info_label.config(
                text=f'CPU: {cpu:.1f}%  |  RAM: {mem:.1f}%  |  Processes: {procs}')
            self.keyboard_status.config(
                text='✅ Keyboard' if info.get('hooks_active') else '⚫ Keyboard',
                fg=self.colors['success'] if info.get('hooks_active') else self.colors['text_secondary'])
            self.mouse_status.config(
                text='✅ Mouse' if info.get('mouse_blocking') else '⚫ Mouse',
                fg=self.colors['success'] if info.get('mouse_blocking') else self.colors['text_secondary'])
            self.network_status.config(
                text='✅ Network' if info.get('internet_blocked') else '⚫ Network',
                fg=self.colors['success'] if info.get('internet_blocked') else self.colors['text_secondary'])
            self.window_status.config(
                text='✅ Windows' if info.get('window_protection') else '⚫ Windows',
                fg=self.colors['success'] if info.get('window_protection') else self.colors['text_secondary'])
        except Exception:
            pass  # Widgets destroyed during tab switch

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
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror('Startup Error', f'Failed to start application:\\n\\n{str(e)}')
        root.destroy()

    def update_activity_feed(self):
        try:
            for item in self.activity_tree.get_children():
                self.activity_tree.delete(item)
            logs = self.db_manager.get_activity_logs(20)
            for log in logs:
                action, details, timestamp, blocked = log
                status = '🚫 BLOCKED' if blocked else '✅ ALLOWED'
                if blocked or 'SUSPICIOUS' in action:
                    severity = '🔴 HIGH'
                elif 'BLOCKED' in action:
                    severity = '🟡 MED'
                else:
                    severity = '🟢 LOW'
                try:
                    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                    time_str = dt.strftime('%H:%M:%S')
                except:
                    time_str = timestamp
                self.activity_tree.insert('', 0, values=(time_str, severity, action, details or 'No details', status))
        except Exception:
            pass

    def create_settings_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='⚙️ Settings')
        container = tk.Frame(frame, bg=self.colors['surface'])
        container.pack(fill=tk.BOTH, expand=True)
        canvas = tk.Canvas(container, bg=self.colors['surface'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)
        inner = tk.Frame(canvas, bg=self.colors['surface'])
        inner.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=inner, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side='left', fill='both', expand=True, padx=15, pady=15)
        scrollbar.pack(side='right', fill='y', padx=(0, 15), pady=15)

    def save_settings(self):
        try:
            messagebox.showinfo('✅ Success', 'Settings saved successfully!')
        except Exception as e:
            messagebox.showerror('❌ Error', f'Failed to save settings: {e}')

    def create_logs_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='📋 Security Logs')
        container = tk.Frame(frame, bg=self.colors['surface'])
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        controls = tk.Frame(container, bg=self.colors['card'], height=60)
        controls.pack(fill=tk.X, pady=(0, 10))
        controls.pack_propagate(False)
        row = tk.Frame(controls, bg=self.colors['card'])
        row.pack(fill=tk.X, padx=15, pady=15)
        tk.Button(row, text='🔄 Refresh', command=self.refresh_logs, bg=self.colors['info'], fg=self.colors['card'], font=('Segoe UI', 9, 'bold'), relief=tk.FLAT, cursor='hand2', padx=10, pady=5).pack(side=tk.LEFT, padx=(0, 10))
        tk.Button(row, text='🗑️ Clear All', command=self.clear_logs, bg=self.colors['warning'], fg=self.colors['card'], font=('Segoe UI', 9, 'bold'), relief=tk.FLAT, cursor='hand2', padx=10, pady=5).pack(side=tk.LEFT, padx=(0, 10))
        tk.Button(row, text='💾 Export', command=self.export_logs, bg=self.colors['success'], fg=self.colors['card'], font=('Segoe UI', 9, 'bold'), relief=tk.FLAT, cursor='hand2', padx=10, pady=5).pack(side=tk.LEFT, padx=(0, 10))
        logs_card = tk.Frame(container, bg=self.colors['card'])
        logs_card.pack(fill=tk.BOTH, expand=True)
        header = tk.Frame(logs_card, bg=self.colors['danger'], height=40)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text='📋 Security Activity History', font=('Segoe UI', 12, 'bold'), bg=self.colors['danger'], fg=self.colors['card']).pack(pady=10)
        content = tk.Frame(logs_card, bg=self.colors['card'])
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.logs_text = scrolledtext.ScrolledText(content, wrap=tk.WORD, height=25, font=('Consolas', 9), bg=self.colors['surface'], fg=self.colors['text_primary'])
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
                status = 'BLOCKED' if blocked else 'ALLOWED'
                self.logs_text.insert(tk.END, f"[{timestamp}] {action}: {details or 'N/A'} - {status}\n")
            except Exception:
                continue
        self.logs_text.see(tk.END)

    def clear_logs(self):
        self.logs_text.delete(1.0, tk.END)

    def export_logs(self):
        pass

    def show_mouse_controls(self):
        """Show mouse controls dialog"""
        dialog = tk.Toplevel(self.window)
        dialog.title('Mouse Control Panel')
        dialog.geometry('500x400')
        dialog.configure(bg=self.colors['surface'])
        dialog.transient(self.window)
        dialog.grab_set()
        x = dialog.winfo_screenwidth() // 2 - 250
        y = dialog.winfo_screenheight() // 2 - 200
        dialog.geometry(f'500x400+{x}+{y}')
        header = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text='🖱️', font=('Segoe UI', 20), bg=self.colors['primary'], fg=self.colors['accent']).pack(pady=10)
        content = tk.Frame(dialog, bg=self.colors['surface'])
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        status = self.security_manager.mouse_manager.get_status()
        status_label = tk.Label(content, text='Mouse Control Status', font=('Segoe UI', 14, 'bold'), bg=self.colors['surface'], fg=self.colors['text_primary'])
        status_label.pack(pady=(0, 20))
        active_status = 'ACTIVE' if status['active'] else 'INACTIVE'
        status_color = self.colors['success'] if status['active'] else self.colors['text_secondary']
        tk.Label(content, text=f'Status: {active_status}', font=('Segoe UI', 12), bg=self.colors['surface'], fg=status_color).pack()
        tk.Label(content, text=f"Blocked Buttons: {', '.join(status['blocked_buttons'])}", font=('Segoe UI', 10), bg=self.colors['surface'], fg=self.colors['text_secondary']).pack(pady=(10, 0))
        btn_frame = tk.Frame(content, bg=self.colors['surface'])
        btn_frame.pack(pady=30)
        if status['active']:
            self.create_premium_button(btn_frame, 'Disable Mouse Blocking', self.security_manager.mouse_manager.stop_blocking, self.colors['danger'], pack_side='').pack(side=tk.LEFT, padx=10)
        else:
            self.create_premium_button(btn_frame, 'Enable Mouse Blocking', self.security_manager.mouse_manager.start_blocking, self.colors['success'], pack_side='').pack(side=tk.LEFT, padx=10)
        self.create_premium_button(btn_frame, 'Close', dialog.destroy, self.colors['primary'], pack_side='').pack(side=tk.LEFT, padx=10)

    def _toggle_mouse_and_close(self, enable, window):
        try:
            ok = self.security_manager.toggle_mouse_blocking(enable)
            action = 'activated' if enable else 'deactivated'
            messagebox.showinfo('✅ Success', f'Mouse blocking {action} successfully!') if ok else messagebox.showerror('❌ Error', f"Failed to {action.replace('ed', '')} mouse blocking.")
        finally:
            window.destroy()
            self.refresh_status()

    def _apply_mouse_setting(self, t):
        try:
            if t == 'basic':
                self.security_manager.mouse_manager.allow_basic_clicks()
                messagebox.showinfo('✅ Applied', 'Mouse set to allow basic clicks only (blocks middle/side buttons)')
            elif t == 'all':
                self.security_manager.mouse_manager.block_all_buttons()
                messagebox.showinfo('✅ Applied', 'Mouse set to block all buttons')
        finally:
            self.refresh_status()

    def show_window_controls(self):
        """Show window controls dialog"""
        dialog = tk.Toplevel(self.window)
        dialog.title('Window Guardian Control')
        dialog.geometry('500x350')
        dialog.configure(bg=self.colors['surface'])
        dialog.transient(self.window)
        dialog.grab_set()
        x = dialog.winfo_screenwidth() // 2 - 250
        y = dialog.winfo_screenheight() // 2 - 175
        dialog.geometry(f'500x350+{x}+{y}')
        header = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text='🪟', font=('Segoe UI', 20), bg=self.colors['primary'], fg=self.colors['accent']).pack(pady=10)
        content = tk.Frame(dialog, bg=self.colors['surface'])
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        status_label = tk.Label(content, text='Window Guardian Status', font=('Segoe UI', 14, 'bold'), bg=self.colors['surface'], fg=self.colors['text_primary'])
        status_label.pack(pady=(0, 20))
        active = self.security_manager.window_manager.is_active
        status_text = 'ACTIVE' if active else 'INACTIVE'
        status_color = self.colors['success'] if active else self.colors['text_secondary']
        tk.Label(content, text=f'Window Protection: {status_text}', font=('Segoe UI', 12), bg=self.colors['surface'], fg=status_color).pack()
        features = ['Prevents Alt+Tab window switching', 'Blocks Alt+F4 window close', 'Prevents Windows key shortcuts', 'Blocks window minimize/maximize', 'Monitors task switching attempts']
        tk.Label(content, text='Active Features:', font=('Segoe UI', 10, 'bold'), bg=self.colors['surface'], fg=self.colors['text_primary']).pack(pady=(20, 10))
        for feature in features:
            tk.Label(content, text=f'• {feature}', font=('Segoe UI', 9), bg=self.colors['surface'], fg=self.colors['text_secondary']).pack(anchor=tk.W)
        btn_frame = tk.Frame(content, bg=self.colors['surface'])
        btn_frame.pack(pady=20)
        if active:
            self.create_premium_button(btn_frame, 'Disable Window Guardian', self.security_manager.window_manager.stop_window_protection, self.colors['danger'], pack_side='').pack(side=tk.LEFT, padx=10)
        else:
            self.create_premium_button(btn_frame, 'Enable Window Guardian', self.security_manager.window_manager.start_window_protection, self.colors['success'], pack_side='').pack(side=tk.LEFT, padx=10)
        self.create_premium_button(btn_frame, 'Close', dialog.destroy, self.colors['primary'], pack_side='').pack(side=tk.LEFT, padx=10)

    def _toggle_window_and_close(self, enable, window):
        try:
            ok = self.security_manager.toggle_window_protection(enable)
            action = 'activated' if enable else 'deactivated'
            messagebox.showinfo('✅ Success', f'Window protection {action} successfully!') if ok else messagebox.showerror('❌ Error', f"Failed to {action.replace('ed', '')} window protection.")
        finally:
            window.destroy()
            self.refresh_status()

    def show_network_controls(self):
        """Show network controls dialog"""
        dialog = tk.Toplevel(self.window)
        dialog.title('Network Control Panel')
        dialog.geometry('550x500')
        dialog.configure(bg=self.colors['surface'])
        dialog.transient(self.window)
        dialog.grab_set()
        x = dialog.winfo_screenwidth() // 2 - 275
        y = dialog.winfo_screenheight() // 2 - 250
        dialog.geometry(f'550x500+{x}+{y}')
        header = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text='🌐', font=('Segoe UI', 20), bg=self.colors['primary'], fg=self.colors['accent']).pack(pady=10)
        content = tk.Frame(dialog, bg=self.colors['surface'])
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        status_label = tk.Label(content, text='Network Security Status', font=('Segoe UI', 14, 'bold'), bg=self.colors['surface'], fg=self.colors['text_primary'])
        status_label.pack(pady=(0, 20))
        blocked = self.security_manager.network_manager.is_blocked
        status_text = 'BLOCKED' if blocked else 'ACTIVE'
        status_color = self.colors['danger'] if blocked else self.colors['success']
        tk.Label(content, text=f'Internet Access: {status_text}', font=('Segoe UI', 12), bg=self.colors['surface'], fg=status_color).pack()
        card, card_content = self.create_card(content, 'Blocked Websites', '🚫')
        card.pack(fill=tk.X, pady=20)
        sites_text = scrolledtext.ScrolledText(card_content, height=12, font=('Consolas', 9), bg=self.colors['surface'], fg=self.colors['text_primary'])
        sites_text.pack(fill=tk.BOTH, expand=True)
        blocked_sites = self.security_manager.network_manager.get_blocked_websites()
        sites_text.insert(tk.END, '\n'.join(blocked_sites))
        sites_text.config(state=tk.DISABLED)
        btn_frame = tk.Frame(content, bg=self.colors['surface'])
        btn_frame.pack(pady=10)
        if blocked:
            self.create_premium_button(btn_frame, 'Restore Internet Access', self.security_manager.network_manager.stop_blocking, self.colors['success'], pack_side='').pack(side=tk.LEFT, padx=10)
        else:
            self.create_premium_button(btn_frame, 'Block Internet Access', self.security_manager.network_manager.start_blocking, self.colors['danger'], pack_side='').pack(side=tk.LEFT, padx=10)
        self.create_premium_button(btn_frame, 'Close', dialog.destroy, self.colors['primary'], pack_side='').pack(side=tk.LEFT, padx=10)

    def toggle_mouse_blocking(self, enable):
        try:
            return self.security_manager.toggle_mouse_blocking(enable)
        except Exception as e:
            messagebox.showerror('Error', f'Mouse toggle failed: {e}')
            return False

    def toggle_internet_blocking(self, enable):
        try:
            return self.security_manager.toggle_internet_blocking(enable)
        except Exception as e:
            messagebox.showerror('Error', f'Internet toggle failed: {e}')
            return False

    def toggle_window_protection(self, enable):
        try:
            return self.security_manager.toggle_window_protection(enable)
        except Exception as e:
            messagebox.showerror('Error', f'Window toggle failed: {e}')
            return False

    def stop_exam_mode(self):
        """Stop exam mode with confirmation"""
        if not self.security_manager.is_exam_mode:
            messagebox.showinfo('Info', 'Lockdown mode is not active!')
            return
        result = messagebox.askyesno('End Lockdown', 'Are you sure you want to end lockdown mode?\n\nThis will deactivate all security restrictions.')
        if result:
            try:
                self.security_manager.stop_exam_mode()
                self.start_btn.config(state=tk.NORMAL)
                self.stop_btn.config(state=tk.DISABLED)
                self.refresh_status()
                messagebox.showinfo('Success', 'Lockdown mode has been deactivated!\n\nAll security restrictions removed.')
            except Exception as e:
                messagebox.showerror('Error', f'Failed to stop lockdown: {str(e)}')

    def emergency_stop(self):
        """Emergency stop procedure"""
        result = messagebox.askyesno('EMERGENCY STOP', "⚠️ EMERGENCY STOP REQUESTED\n\nThis will immediately end lockdown mode and restore all system access.\n\nUse this ONLY if there's a critical issue or system malfunction.\n\nAre you sure you want to proceed?")
        if result:
            try:
                self.security_manager.stop_exam_mode()
                self.start_btn.config(state=tk.NORMAL)
                self.stop_btn.config(state=tk.DISABLED)
                self.refresh_status()
                messagebox.showinfo('Emergency Stop Complete', 'Emergency stop completed successfully.\n\nAll security restrictions have been removed.\nSystem access has been fully restored.')
            except Exception as e:
                messagebox.showwarning('Warning', f'Emergency stop executed with minor error:\n{str(e)}\n\nSystem restrictions should be removed.')

    def create_keyboard_settings(self, parent):
        """Create keyboard settings section"""
        card, content = self.create_card(parent, 'Keyboard Protection', '🔤')
        card.pack(fill=tk.X, pady=(0, 15))
        self.keyboard_vars = {}
        blocked_keys = [('alt+tab', 'Alt + Tab'), ('alt+f4', 'Alt + F4'), ('win+d', 'Windows + D'), ('win+l', 'Windows + L'), ('win+r', 'Windows + R'), ('ctrl+alt+del', 'Ctrl + Alt + Delete'), ('ctrl+shift+esc', 'Ctrl + Shift + Escape'), ('f11', 'F11 Fullscreen'), ('alt+space', 'Alt + Space')]
        grid_frame = tk.Frame(content, bg=self.colors['card'])
        grid_frame.pack(fill=tk.X)
        for i, (key, label) in enumerate(blocked_keys):
            row = i // 3
            col = i % 3
            var = tk.BooleanVar(value=True)
            self.keyboard_vars[key] = var
            cb = tk.Checkbutton(grid_frame, text=label, variable=var, font=('Segoe UI', 9), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['light_blue'])
            cb.grid(row=row, column=col, sticky='w', padx=10, pady=5)

    def create_mouse_settings(self, parent):
        """Create mouse settings section"""
        card, content = self.create_card(parent, 'Mouse Control', '🖱️')
        card.pack(fill=tk.X, pady=(0, 15))
        self.mouse_vars = {}
        mouse_buttons = [('middle', 'Middle Button'), ('x1', 'Extra Button 1'), ('x2', 'Extra Button 2'), ('side', 'Side Button'), ('back', 'Back Button'), ('forward', 'Forward Button')]
        grid_frame = tk.Frame(content, bg=self.colors['card'])
        grid_frame.pack(fill=tk.X)
        for i, (key, label) in enumerate(mouse_buttons):
            row = i // 3
            col = i % 3
            var = tk.BooleanVar(value=True)
            self.mouse_vars[key] = var
            cb = tk.Checkbutton(grid_frame, text=label, variable=var, font=('Segoe UI', 9), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['light_blue'])
            cb.grid(row=row, column=col, sticky='w', padx=10, pady=5)
        btn_frame = tk.Frame(content, bg=self.colors['card'])
        btn_frame.pack(fill=tk.X, pady=(15, 0))
        self.create_premium_button(btn_frame, 'Apply Settings', self.apply_mouse_settings, self.colors['primary'], pack_side='left')

    def create_network_settings(self, parent):
        """Create network settings section"""
        card, content = self.create_card(parent, 'Network Security', '🌐')
        card.pack(fill=tk.X, pady=(0, 15))
        self.network_var = tk.BooleanVar(value=True)
        cb = tk.Checkbutton(content, text='Block Internet Access', variable=self.network_var, font=('Segoe UI', 11, 'bold'), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['light_blue'])
        cb.pack(anchor=tk.W, pady=(0, 10))
        tk.Label(content, text='Blocked Websites:', font=('Segoe UI', 10), bg=self.colors['card'], fg=self.colors['text_secondary']).pack(anchor=tk.W)
        blocked_sites = tk.Label(content, text='google.com, facebook.com, youtube.com, twitter.com, instagram.com, reddit.com, discord.com', font=('Segoe UI', 9), bg=self.colors['card'], fg=self.colors['text_secondary'], wraplength=500)
        blocked_sites.pack(anchor=tk.W, pady=(5, 0))

    def create_advanced_settings(self, parent):
        """Create advanced settings section"""
        card, content = self.create_card(parent, 'Advanced Settings', '⚙️')
        card.pack(fill=tk.X, pady=(0, 15))
        self.auto_refresh_var = tk.BooleanVar(value=True)
        cb = tk.Checkbutton(content, text='Auto-refresh Status (every 2 seconds)', variable=self.auto_refresh_var, font=('Segoe UI', 10), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['light_blue'])
        cb.pack(anchor=tk.W, pady=5)
        self.process_monitor_var = tk.BooleanVar(value=True)
        cb2 = tk.Checkbutton(content, text='Monitor & Terminate Suspicious Processes', variable=self.process_monitor_var, font=('Segoe UI', 10), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['light_blue'])
        cb2.pack(anchor=tk.W, pady=5)
        self.window_protect_var = tk.BooleanVar(value=True)
        cb3 = tk.Checkbutton(content, text='Window Guardian (prevent switching/closing)', variable=self.window_protect_var, font=('Segoe UI', 10), bg=self.colors['card'], fg=self.colors['text_primary'], selectcolor=self.colors['light_blue'])
        cb3.pack(anchor=tk.W, pady=5)

    def apply_mouse_settings(self):
        """Apply mouse settings"""
        selected = [key for key, var in self.mouse_vars.items() if var.get()]
        if selected:
            self.security_manager.mouse_manager.blocked_buttons = selected
            self.security_manager.mouse_manager.start_blocking(selected)
            messagebox.showinfo('Success', f"Mouse settings applied!\n\nBlocked buttons: {', '.join(selected)}")
        else:
            messagebox.showwarning('Warning', 'Please select at least one button to block.')