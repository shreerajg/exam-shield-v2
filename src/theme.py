import tkinter as tk
from tkinter import ttk
import sys
import os
import math

class ExamShieldTheme:
    """Premium 3D theme system for Exam Shield Pro"""

    def __init__(self, theme_mode="dark"):
        self.theme_mode = theme_mode
        self.setup_theme()

    def setup_theme(self):
        """Initialize theme configuration"""
        if self.theme_mode == "dark":
            self.colors = self.get_dark_theme()
        elif self.theme_mode == "pink":
            self.colors = self.get_pink_theme()
        else:
            self.colors = self.get_light_theme()
        
        self.fonts = self.get_font_system()
        self.animations = self.get_animation_config()
    
    def get_light_theme(self):
        """Premium light theme — deep navy + electric blue + gold"""
        return {
            'primary':        '#1a56db',
            'primary_light':  '#3b82f6',
            'primary_dark':   '#1e3a8a',
            'primary_hover':  '#1d4ed8',
            'secondary':      '#7c3aed',
            'secondary_light':'#a78bfa',
            'secondary_dark': '#5b21b6',
            'accent':         '#f59e0b',
            'accent_light':   '#fcd34d',
            'accent_dark':    '#d97706',
            'success':        '#059669',
            'success_light':  '#34d399',
            'warning':        '#d97706',
            'danger':         '#dc2626',
            'danger_light':   '#f87171',
            'info':           '#0284c7',
            'white':          '#ffffff',
            'gray_50':        '#f8fafc',
            'gray_100':       '#f1f5f9',
            'gray_200':       '#e2e8f0',
            'gray_300':       '#cbd5e1',
            'gray_400':       '#94a3b8',
            'gray_500':       '#64748b',
            'gray_600':       '#475569',
            'gray_700':       '#334155',
            'gray_800':       '#1e293b',
            'gray_900':       '#0f172a',
            'background':     '#eef2ff',
            'surface':        '#f8faff',
            'card':           '#ffffff',
            'card_hover':     '#f0f4ff',
            'sidebar':        '#1e293b',
            'sidebar_hover':  '#334155',
            'text_primary':   '#0f172a',
            'text_secondary': '#475569',
            'text_muted':     '#94a3b8',
            'text_inverse':   '#ffffff',
            'border':         '#c7d7fe',
            'border_light':   '#e0e7ff',
            'border_focus':   '#1a56db',
            'btn_highlight':  '#ffffff',
            'btn_shadow':     '#0d2f8c',
            'btn_edge':       '#1442b5',
            'gradient_start': '#1a56db',
            'gradient_end':   '#7c3aed',
            'gradient_mid':   '#2563eb',
            'shadow':         '#00000015',
            'shadow_dark':    '#00000040',
            'neon_glow':      '#3b82f6',
            'neon_glow2':     '#7c3aed',
        }
    
    def get_dark_theme(self):
        """Premium dark theme — deep space + electric indigo + gold"""
        return {
            'primary':        '#6366f1',
            'primary_light':  '#818cf8',
            'primary_dark':   '#4338ca',
            'primary_hover':  '#4f46e5',
            'secondary':      '#8b5cf6',
            'secondary_light':'#a78bfa',
            'secondary_dark': '#6d28d9',
            'accent':         '#f59e0b',
            'accent_light':   '#fcd34d',
            'accent_dark':    '#d97706',
            'success':        '#10b981',
            'success_light':  '#34d399',
            'warning':        '#f59e0b',
            'danger':         '#ef4444',
            'danger_light':   '#f87171',
            'info':           '#06b6d4',
            'white':          '#ffffff',
            'gray_50':        '#0d1117',
            'gray_100':       '#161b22',
            'gray_200':       '#21262d',
            'gray_300':       '#30363d',
            'gray_400':       '#484f58',
            'gray_500':       '#6e7681',
            'gray_600':       '#8b949e',
            'gray_700':       '#b1bac4',
            'gray_800':       '#c9d1d9',
            'gray_900':       '#e6edf3',
            'background':     '#090c14',
            'surface':        '#0d1117',
            'card':           '#161b22',
            'card_hover':     '#1c2330',
            'sidebar':        '#080b12',
            'sidebar_hover':  '#0d1117',
            'text_primary':   '#e6edf3',
            'text_secondary': '#8b949e',
            'text_muted':     '#6e7681',
            'text_inverse':   '#0d1117',
            'border':         '#30363d',
            'border_light':   '#21262d',
            'border_focus':   '#6366f1',
            'btn_highlight':  '#7b7ffa',
            'btn_shadow':     '#1e1b4b',
            'btn_edge':       '#312e81',
            'gradient_start': '#1e1b4b',
            'gradient_end':   '#312e81',
            'gradient_mid':   '#4338ca',
            'shadow':         '#00000050',
            'shadow_dark':    '#00000080',
            'neon_glow':      '#6366f1',
            'neon_glow2':     '#8b5cf6',
        }
    
    def get_pink_theme(self):
        """Premium pink theme — hot pink + violet + gold"""
        return {
            'primary':        '#db2777',
            'primary_light':  '#f472b6',
            'primary_dark':   '#9d174d',
            'primary_hover':  '#be185d',
            'secondary':      '#7c3aed',
            'secondary_light':'#a78bfa',
            'secondary_dark': '#5b21b6',
            'accent':         '#f59e0b',
            'accent_light':   '#fcd34d',
            'accent_dark':    '#d97706',
            'success':        '#059669',
            'success_light':  '#34d399',
            'warning':        '#d97706',
            'danger':         '#dc2626',
            'danger_light':   '#f87171',
            'info':           '#0284c7',
            'white':          '#ffffff',
            'gray_50':        '#fdf2f8',
            'gray_100':       '#fce7f3',
            'gray_200':       '#fbcfe8',
            'gray_300':       '#f9a8d4',
            'gray_400':       '#f472b6',
            'gray_500':       '#ec4899',
            'gray_600':       '#db2777',
            'gray_700':       '#be185d',
            'gray_800':       '#9d174d',
            'gray_900':       '#831843',
            'background':     '#fff0f7',
            'surface':        '#fff5f9',
            'card':           '#ffffff',
            'card_hover':     '#fff0f9',
            'sidebar':        '#831843',
            'sidebar_hover':  '#9d174d',
            'text_primary':   '#500724',
            'text_secondary': '#9d174d',
            'text_muted':     '#f472b6',
            'text_inverse':   '#ffffff',
            'border':         '#fbb6ce',
            'border_light':   '#fce7f3',
            'border_focus':   '#db2777',
            'btn_highlight':  '#ff85c0',
            'btn_shadow':     '#700d38',
            'btn_edge':       '#a01050',
            'gradient_start': '#db2777',
            'gradient_end':   '#7c3aed',
            'gradient_mid':   '#c026d3',
            'shadow':         '#db277720',
            'shadow_dark':    '#db277750',
            'neon_glow':      '#ec4899',
            'neon_glow2':     '#7c3aed',
        }
    
    def get_font_system(self):
        """Professional font system"""
        f = self.get_system_font()
        return {
            'heading':    (f, 28, 'bold'),
            'title':      (f, 20, 'bold'),
            'subtitle':   (f, 16, 'bold'),
            'body':       (f, 11, 'normal'),
            'body_bold':  (f, 11, 'bold'),
            'body_large': (f, 13, 'normal'),
            'caption':    (f, 10, 'normal'),
            'small':      (f, 9,  'normal'),
            'mono':       ('Consolas', 10, 'normal'),
            'mono_small': ('Consolas', 9,  'normal'),
            'nav':        (f, 10, 'bold'),
            'btn':        (f, 11, 'bold'),
            'btn_large':  (f, 13, 'bold'),
        }
    
    def get_system_font(self):
        """Get appropriate system font"""
        if sys.platform.startswith('win'):
            return 'Segoe UI'
        elif sys.platform.startswith('darwin'):
            return 'SF Pro Display'
        else:
            return 'Ubuntu'
    
    def get_animation_config(self):
        """Animation and transition configuration"""
        return {
            'duration_fast': 150,
            'duration_normal': 250,
            'duration_slow': 400,
            'easing': 'ease-out',
            'hover_scale': 1.02,
            'button_press_scale': 0.98,
        }
    
    def apply_ttk_theme(self, root):
        """Apply theme to ttk widgets"""
        style = ttk.Style()
        
        # Use modern theme if available
        try:
            import sv_ttk
            if self.theme_mode == "dark":
                sv_ttk.set_theme("dark")
            else:
                sv_ttk.set_theme("light")
        except ImportError:
            # Fallback to built-in themes
            style.theme_use('clam')
        
        # Configure custom styles
        self.configure_button_styles(style)
        self.configure_entry_styles(style)
        self.configure_frame_styles(style)
        self.configure_treeview_styles(style)
        self.configure_notebook_styles(style)
    
    def configure_button_styles(self, style):
        """Configure button styles"""
        for name, bg, hover in [
            ('Primary', self.colors['primary'],  self.colors['primary_hover']),
            ('Success', self.colors['success'],  self.colors['success_light']),
            ('Danger',  self.colors['danger'],   self.colors['danger_light']),
            ('Warning', self.colors['warning'],  self.colors['accent']),
            ('Accent',  self.colors['accent'],   self.colors['accent_dark']),
        ]:
            style.configure(f'{name}.TButton',
                            background=bg,
                            foreground=self.colors['text_inverse'],
                            font=self.fonts['body_bold'],
                            borderwidth=0,
                            focuscolor='none',
                            relief='flat')
            style.map(f'{name}.TButton',
                      background=[('active', hover),
                                  ('pressed', self.colors['primary_dark'])])
    
    def configure_entry_styles(self, style):
        """Configure entry widget styles"""
        style.configure('Modern.TEntry',
                       fieldbackground=self.colors['surface'],
                       foreground=self.colors['text_primary'],
                       bordercolor=self.colors['border'],
                       focuscolor=self.colors['border_focus'],
                       insertcolor=self.colors['primary'],
                       font=self.fonts['body'])
    
    def configure_frame_styles(self, style):
        """Configure frame styles"""
        style.configure('Card.TFrame',
                       background=self.colors['card'],
                       relief='flat',
                       borderwidth=1)
        
        style.configure('Sidebar.TFrame',
                       background=self.colors['sidebar'])
    
    def configure_treeview_styles(self, style):
        """Configure treeview styles"""
        style.configure('Modern.Treeview',
                       background=self.colors['surface'],
                       foreground=self.colors['text_primary'],
                       fieldbackground=self.colors['surface'],
                       font=self.fonts['body'])
        
        style.configure('Modern.Treeview.Heading',
                       background=self.colors['gray_100'],
                       foreground=self.colors['text_primary'],
                       font=self.fonts['body_bold'])
    
    def configure_notebook_styles(self, style):
        """Configure notebook styles"""
        style.configure('Modern.TNotebook',
                       background=self.colors['background'],
                       borderwidth=0)
        
        style.configure('Modern.TNotebook.Tab',
                       background=self.colors['surface'],
                       foreground=self.colors['text_secondary'],
                       font=self.fonts['body'],
                       padding=(20, 10))
        
        style.map('Modern.TNotebook.Tab',
                 background=[('selected', self.colors['primary']),
                           ('active', self.colors['gray_100'])],
                 foreground=[('selected', self.colors['text_inverse']),
                           ('active', self.colors['text_primary'])])

class AnimationManager:
    """Handle smooth animations and transitions"""

    # ── Easing utilities ────────────────────────────────────────────────────

    @staticmethod
    def _ease_out_cubic(t):
        """Cubic ease-out: starts fast, decelerates to stop."""
        return 1 - (1 - t) ** 3

    @staticmethod
    def _ease_in_out(t):
        """Smooth symmetric ease."""
        return t * t * (3 - 2 * t)

    @staticmethod
    def _ease_elastic(t):
        """Elastic overshoot then settle."""
        if t == 0 or t == 1:
            return t
        import math
        p = 0.3
        return (2 ** (-10 * t)) * math.sin((t - p / 4) * (2 * math.pi) / p) + 1

    @staticmethod
    def _hex_to_rgb(h):
        h = h.lstrip('#')
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def _rgb_to_hex(r, g, b):
        return f'#{int(r):02x}{int(g):02x}{int(b):02x}'

    def __init__(self, root):
        self.root = root
        self.animations = {}

    # ── Fade ────────────────────────────────────────────────────────────────

    def fade_in(self, widget, duration=300):
        """Fade-in with ease-out easing."""
        try:
            widget.attributes('-alpha', 0.0)
        except tk.TclError:
            return
        self._animate_alpha(widget, 0.0, 1.0, duration)

    def fade_out(self, widget, duration=300, callback=None):
        """Fade-out animation."""
        self._animate_alpha(widget, 1.0, 0.0, duration, callback)

    def _animate_alpha(self, widget, start, end, duration, callback=None):
        steps = 30
        step_ms = max(1, duration // steps)

        def step(i):
            if i > steps:
                if callback:
                    callback()
                return
            t = self._ease_out_cubic(i / steps)
            alpha = start + (end - start) * t
            try:
                widget.attributes('-alpha', alpha)
                widget.after(step_ms, lambda: step(i + 1))
            except tk.TclError:
                pass

        step(0)

    # ── Slide-in ────────────────────────────────────────────────────────────

    def slide_in(self, widget, direction='left', duration=350, distance=60):
        """Slide a Frame/widget in from direction ('left','right','top','bottom').

        Works by temporarily placing the widget off-screen with place(), animating
        it to its natural position, then restoring normal geometry management.
        """
        widget.update_idletasks()
        w = widget.winfo_width() or 200
        h = widget.winfo_height() or 100
        natural_x = widget.winfo_x()
        natural_y = widget.winfo_y()

        offsets = {
            'left':   (-distance, 0),
            'right':  (distance,  0),
            'top':    (0, -distance),
            'bottom': (0,  distance),
        }
        dx, dy = offsets.get(direction, (-distance, 0))

        steps = 28
        step_ms = max(1, duration // steps)

        def step(i):
            if i > steps:
                try:
                    widget.place_forget()
                except Exception:
                    pass
                return
            t = self._ease_out_cubic(i / steps)
            cx = natural_x + dx * (1 - t)
            cy = natural_y + dy * (1 - t)
            try:
                widget.place(x=int(cx), y=int(cy), width=w, height=h)
                widget.after(step_ms, lambda: step(i + 1))
            except tk.TclError:
                pass

        step(0)

    # ── Shake (error feedback) ───────────────────────────────────────────────

    def shake(self, widget, intensity=8, cycles=4, duration=320):
        """Horizontal shake animation – use on login frames on error."""
        widget.update_idletasks()
        orig_x = widget.winfo_x()
        orig_y = widget.winfo_y()
        w = widget.winfo_width()
        h = widget.winfo_height()

        steps = cycles * 2
        step_ms = max(1, duration // steps)
        offsets = []
        for i in range(steps):
            sign = 1 if i % 2 == 0 else -1
            fade = 1 - i / steps
            offsets.append(int(sign * intensity * fade))
        offsets.append(0)  # settle

        def step(i):
            if i >= len(offsets):
                try:
                    widget.place_forget()
                except Exception:
                    pass
                return
            try:
                widget.place(x=orig_x + offsets[i], y=orig_y, width=w, height=h)
                widget.after(step_ms, lambda: step(i + 1))
            except tk.TclError:
                pass

        step(0)

    # ── Bounce entrance ─────────────────────────────────────────────────────

    def bounce_in(self, widget, duration=500):
        """Elastic bounce-in – good for status labels or icons."""
        widget.update_idletasks()
        orig_x = widget.winfo_x()
        orig_y = widget.winfo_y()
        w = widget.winfo_width()
        h = widget.winfo_height()
        drop = 30  # pixels above final position

        steps = 40
        step_ms = max(1, duration // steps)

        def step(i):
            if i > steps:
                try:
                    widget.place_forget()
                except Exception:
                    pass
                return
            t = self._ease_elastic(i / steps)
            cy = orig_y + drop * (1 - t) - drop
            try:
                widget.place(x=orig_x, y=int(cy), width=w, height=h)
                widget.after(step_ms, lambda: step(i + 1))
            except tk.TclError:
                pass

        step(0)

    # ── Typewriter text reveal ───────────────────────────────────────────────

    def typewriter(self, label, full_text, char_delay=45):
        """Reveal *full_text* character-by-character on a tk.Label."""
        if hasattr(label, '_typewriter_id') and label._typewriter_id:
            try:
                label.after_cancel(label._typewriter_id)
            except Exception:
                pass

        def reveal(pos):
            try:
                label.config(text=full_text[:pos])
                if pos < len(full_text):
                    label._typewriter_id = label.after(char_delay, lambda: reveal(pos + 1))
                else:
                    label._typewriter_id = None
            except tk.TclError:
                pass

        label._typewriter_id = None
        reveal(0)

    # ── Animated number counter ──────────────────────────────────────────────

    def count_up(self, label, start, end, duration=800, suffix='', prefix=''):
        """Animate a numeric label from *start* to *end*."""
        if hasattr(label, '_counter_id') and label._counter_id:
            try:
                label.after_cancel(label._counter_id)
            except Exception:
                pass

        steps = 40
        step_ms = max(1, duration // steps)

        def step(i):
            if i > steps:
                try:
                    label.config(text=f'{prefix}{int(end)}{suffix}')
                except tk.TclError:
                    pass
                label._counter_id = None
                return
            t = self._ease_out_cubic(i / steps)
            value = start + (end - start) * t
            try:
                label.config(text=f'{prefix}{int(value)}{suffix}')
                label._counter_id = label.after(step_ms, lambda: step(i + 1))
            except tk.TclError:
                pass

        label._counter_id = None
        step(0)

    # ── Entry focus glow ─────────────────────────────────────────────────────

    def bind_entry_glow(self, entry, normal_color='white', focus_color='#dbeafe'):
        """Animate background of an Entry on focus/blur."""
        def _animate_bg(from_c, to_c):
            try:
                fc = self._hex_to_rgb(from_c)
                tc = self._hex_to_rgb(to_c)
            except Exception:
                return
            steps = 12
            step_ms = 15

            def step(i):
                if i > steps:
                    return
                t = i / steps
                r = fc[0] + (tc[0] - fc[0]) * t
                g = fc[1] + (tc[1] - fc[1]) * t
                b = fc[2] + (tc[2] - fc[2]) * t
                try:
                    entry.config(bg=self._rgb_to_hex(r, g, b))
                    entry.after(step_ms, lambda: step(i + 1))
                except tk.TclError:
                    pass

            step(0)

        entry.bind('<FocusIn>',  lambda e: _animate_bg(normal_color, focus_color), add='+')
        entry.bind('<FocusOut>', lambda e: _animate_bg(focus_color,  normal_color), add='+')

    # ── Canvas / label colour pulse ──────────────────────────────────────────

    def pulse_text_color(self, canvas, item_id, color1, color2, duration=1500):
        """Pulse text color between two hex colors on a canvas item."""
        try:
            c1 = self._hex_to_rgb(color1)
            c2 = self._hex_to_rgb(color2)
        except Exception:
            return

        steps = 30
        step_ms = max(1, duration // steps)

        def animate(forward=True, i=0):
            if i <= steps:
                t = i / steps
                ratio = t if forward else 1 - t
                r = c1[0] + (c2[0] - c1[0]) * ratio
                g = c1[1] + (c2[1] - c1[1]) * ratio
                b = c1[2] + (c2[2] - c1[2]) * ratio
                try:
                    canvas.itemconfig(item_id, fill=self._rgb_to_hex(r, g, b))
                    self.root.after(step_ms, lambda: animate(forward, i + 1))
                except tk.TclError:
                    pass
            else:
                self.root.after(step_ms, lambda: animate(not forward, 0))

        animate(True, 0)

    def pulse_label_color(self, label, color1, color2, duration=1500):
        """Pulse text color between two hex colors on a standard Label."""
        try:
            c1 = self._hex_to_rgb(color1)
            c2 = self._hex_to_rgb(color2)
        except Exception:
            return

        steps = 30
        step_ms = max(1, duration // steps)

        if hasattr(label, '_pulse_after_id') and label._pulse_after_id:
            try:
                label.after_cancel(label._pulse_after_id)
            except Exception:
                pass

        def animate(forward=True, i=0):
            if i <= steps:
                t = i / steps
                ratio = t if forward else 1 - t
                r = c1[0] + (c2[0] - c1[0]) * ratio
                g = c1[1] + (c2[1] - c1[1]) * ratio
                b = c1[2] + (c2[2] - c1[2]) * ratio
                try:
                    label.config(fg=self._rgb_to_hex(r, g, b))
                    label._pulse_after_id = label.after(step_ms, lambda: animate(forward, i + 1))
                except tk.TclError:
                    pass
            else:
                label._pulse_after_id = label.after(step_ms, lambda: animate(not forward, 0))

        animate(True, 0)

    # ── Button shimmer hover ─────────────────────────────────────────────────

    def bind_shimmer_hover(self, button, base_color, hover_color):
        """Smooth colour-transition hover effect on a tk.Button."""
        try:
            c1 = self._hex_to_rgb(base_color)
            c2 = self._hex_to_rgb(hover_color)
        except Exception:
            return

        steps = 10
        step_ms = 12
        _anim_id = [None]

        def _transition(fc, tc, i):
            if i > steps:
                return
            t = i / steps
            r = fc[0] + (tc[0] - fc[0]) * t
            g = fc[1] + (tc[1] - fc[1]) * t
            b = fc[2] + (tc[2] - fc[2]) * t
            try:
                button.config(bg=self._rgb_to_hex(r, g, b))
                _anim_id[0] = button.after(step_ms, lambda: _transition(fc, tc, i + 1))
            except tk.TclError:
                pass

        def on_enter(e):
            if _anim_id[0]:
                try:
                    button.after_cancel(_anim_id[0])
                except Exception:
                    pass
            _transition(c1, c2, 0)

        def on_leave(e):
            if _anim_id[0]:
                try:
                    button.after_cancel(_anim_id[0])
                except Exception:
                    pass
            _transition(c2, c1, 0)

        button.bind('<Enter>', on_enter, add='+')
        button.bind('<Leave>', on_leave, add='+')

    # ── Button press ripple ──────────────────────────────────────────────────

    def button_press_effect(self, button):
        """Quick press animation: brief darken + relief change."""
        try:
            orig = button.cget('bg')
            rgb = self._hex_to_rgb(orig)
            darker = self._rgb_to_hex(
                max(0, int(rgb[0] * 0.75)),
                max(0, int(rgb[1] * 0.75)),
                max(0, int(rgb[2] * 0.75))
            )
            button.config(bg=darker, relief='sunken')
            button.after(120, lambda: button.config(bg=orig, relief='flat'))
        except Exception:
            pass

class ModernComponents:
    """Custom modern UI components"""
    
    def __init__(self, theme):
        self.theme = theme
        
    def bind_hover(self, widget, normal_bg, hover_bg):
        """Bind smooth animated hover colour transition to a widget."""
        anim = AnimationManager(widget)
        anim.bind_shimmer_hover(widget, normal_bg, hover_bg)
    
    def create_card(self, parent, title=None, **kwargs):
        """Create a modern card component"""
        card_frame = tk.Frame(parent, 
                             bg=self.theme.colors['card'],
                             relief='flat',
                             bd=0,
                             **kwargs)
        
        if title:
            title_label = tk.Label(card_frame,
                                  text=title,
                                  font=self.theme.fonts['subtitle'],
                                  bg=self.theme.colors['card'],
                                  fg=self.theme.colors['text_primary'])
            title_label.pack(anchor='w', padx=20, pady=(20, 10))
        
        return card_frame
    
    def create_icon_button(self, parent, icon, text, command, style='primary'):
        """Create modern icon button with animated hover."""
        colors = {
            'primary': (self.theme.colors['primary'], self.theme.colors['text_inverse']),
            'success': (self.theme.colors['success'], self.theme.colors['text_inverse']),
            'danger': (self.theme.colors['danger'], self.theme.colors['text_inverse']),
            'warning': (self.theme.colors['warning'], self.theme.colors['text_inverse']),
        }

        bg_color, fg_color = colors.get(style, colors['primary'])
        hover_colors = {
            'primary': self.theme.colors['primary_hover'],
            'success': self.theme.colors['secondary_dark'],
            'danger':  '#c0392b',
            'warning': '#e67e22',
        }
        hover_bg = hover_colors.get(style, self.theme.colors['primary_hover'])

        button = tk.Button(parent,
                           text=f"{icon}  {text}",
                           command=command,
                           bg=bg_color,
                           fg=fg_color,
                           font=self.theme.fonts['body_bold'],
                           relief='flat',
                           bd=0,
                           cursor='hand2',
                           padx=20,
                           pady=12)

        anim = AnimationManager(button)
        anim.bind_shimmer_hover(button, bg_color, hover_bg)
        # Press feedback
        button.bind('<ButtonPress-1>', lambda e: anim.button_press_effect(button), add='+')

        return button
    
    def create_status_indicator(self, parent, status='inactive'):
        """Create modern status indicator"""
        colors = {
            'active': self.theme.colors['success'],
            'inactive': self.theme.colors['gray_400'],
            'warning': self.theme.colors['warning'],
            'danger': self.theme.colors['danger']
        }
        
        indicator = tk.Label(parent,
                           text="●",
                           font=('Segoe UI', 12),
                           fg=colors.get(status, colors['inactive']),
                           bg=parent.cget('bg') if hasattr(parent, 'cget') else self.theme.colors['surface'])
        
        return indicator
    
    def create_progress_ring(self, parent, value=0, max_value=100):
        """Create modern circular progress indicator"""
        # This would require custom drawing with tkinter Canvas
        # For now, return a simple progress bar
        progress = ttk.Progressbar(parent,
                                  mode='determinate',
                                  value=value,
                                  maximum=max_value)
        return progress

# Theme presets
THEMES = {
    'light': ExamShieldTheme('light'),
    'dark':  ExamShieldTheme('dark'),
    'pink':  ExamShieldTheme('pink'),
}

def get_theme(theme_name='dark'):
    """Get theme instance"""
    return THEMES.get(theme_name, THEMES['dark'])


# ============================================================
#  GRADIENT CANVAS HELPER
# ============================================================

def create_gradient_canvas(parent, width, height, color1, color2,
                           direction='vertical'):
    """Return a Canvas with a smooth two-color gradient."""
    canvas = tk.Canvas(parent, width=width, height=height, highlightthickness=0)
    r1,g1,b1 = int(color1[1:3],16), int(color1[3:5],16), int(color1[5:7],16)
    r2,g2,b2 = int(color2[1:3],16), int(color2[3:5],16), int(color2[5:7],16)
    if direction == 'vertical':
        for i in range(height):
            t = i / height
            canvas.create_line(0, i, width, i,
                               fill=f'#{int(r1+(r2-r1)*t):02x}{int(g1+(g2-g1)*t):02x}{int(b1+(b2-b1)*t):02x}',
                               width=1)
    else:
        for i in range(width):
            t = i / width
            canvas.create_line(i, 0, i, height,
                               fill=f'#{int(r1+(r2-r1)*t):02x}{int(g1+(g2-g1)*t):02x}{int(b1+(b2-b1)*t):02x}',
                               width=1)
    return canvas


# ============================================================
#  3D BUTTON
# ============================================================

class Button3D:
    """
    Premium 3-D canvas button.
    Features: gradient face, top-left highlight bevel,
    bottom-right shadow, glow ring, animated hover/press.
    """

    def __init__(self, parent, text, command=None,
                 base_color='#6366f1', text_color='#ffffff',
                 icon='', width=180, height=44, style='primary',
                 font=None, glow=False, glow_color=None,
                 corner_radius=10, theme_colors=None):
        self.command    = command
        self.text       = text
        self.icon       = icon
        self.base_color = base_color
        self.text_color = text_color
        self.width      = width
        self.height     = height
        self.style      = style
        self.font       = font or ('Segoe UI', 11, 'bold')
        self.glow       = glow
        self.glow_color = glow_color or base_color
        self.cr         = corner_radius
        self.tc         = theme_colors or {}
        self._pressed   = False
        self._hovered   = False
        self._disabled  = False
        pad = 8
        self._pad = pad
        self.canvas = tk.Canvas(
            parent, width=width+pad*2, height=height+pad*2,
            bg=parent.cget('bg'), highlightthickness=0, cursor='hand2')
        self.ox = pad; self.oy = pad
        self._draw(); self._bind()

    def pack(self, **kw):  self.canvas.pack(**kw)
    def grid(self, **kw):  self.canvas.grid(**kw)
    def place(self, **kw): self.canvas.place(**kw)

    @staticmethod
    def _h2r(h):
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def _r2h(r, g, b):
        return f'#{int(max(0,min(255,r))):02x}{int(max(0,min(255,g))):02x}{int(max(0,min(255,b))):02x}'

    def _lighten(self, col, a=40):
        r,g,b = self._h2r(col); return self._r2h(r+a, g+a, b+a)

    def _darken(self, col, a=40):
        r,g,b = self._h2r(col); return self._r2h(r-a, g-a, b-a)

    def _mix(self, c1, c2, t):
        r1,g1,b1 = self._h2r(c1); r2,g2,b2 = self._h2r(c2)
        return self._r2h(r1+(r2-r1)*t, g1+(g2-g1)*t, b1+(b2-b1)*t)

    def _rrect(self, c, x0, y0, x1, y1, r, **kw):
        pts = [x0+r,y0, x1-r,y0, x1,y0, x1,y0+r,
               x1,y1-r, x1,y1, x1-r,y1, x0+r,y1,
               x0,y1, x0,y1-r, x0,y0+r, x0,y0]
        return c.create_polygon(pts, smooth=True, **kw)

    def _draw(self):
        c = self.canvas; c.delete('all')
        x0, y0 = self.ox, self.oy
        x1, y1 = x0+self.width, y0+self.height
        r = self.cr; bc = self.base_color
        pressed = self._pressed; hovered = self._hovered
        canvas_bg = c.cget('bg')

        # glow ring
        if hovered or self.glow:
            gs = 7 if hovered else 4
            for s in range(gs, 0, -1):
                t = (gs-s)/gs
                col = self._mix(self.glow_color, canvas_bg, 0.5+0.5*t)
                self._rrect(c, x0-s, y0-s, x1+s, y1+s, r+s, fill=col, outline='')

        # drop shadow
        if not pressed:
            for i in range(5, 0, -1):
                shadow = self._mix(self._darken(bc, 60), canvas_bg, i/5)
                self._rrect(c, x0+i, y0+i+1, x1+i, y1+i+1, r, fill=shadow, outline='')

        # face gradient
        if pressed:
            face_hi = self._darken(bc, 25); face_lo = self._darken(bc, 40); ox,oy = 2,3
        elif hovered:
            face_hi = self._lighten(bc, 22); face_lo = self._lighten(bc, 5);  ox,oy = 0,-1
        else:
            face_hi = self._lighten(bc, 12); face_lo = self._darken(bc, 12);  ox,oy = 0,0

        self._rrect(c, x0+ox, y0+oy, x1+ox, y1+oy, r, fill=face_hi, outline='')
        mid_y = y0+oy+int((y1-y0)*0.45)
        c.create_rectangle(x0+ox, mid_y, x1+ox, y1+oy, fill=face_lo, outline='')
        self._rrect(c, x0+ox, y0+oy, x1+ox, y1+oy, r, fill='',
                    outline=self._darken(bc, 35), width=1)

        # highlight bevel
        if not pressed:
            hi = self._lighten(bc, 65)
            c.create_line(x0+ox+r, y0+oy+1, x1+ox-r, y0+oy+1, fill=hi, width=2)
            c.create_line(x0+ox+1, y0+oy+r, x0+ox+1, y1+oy-r,
                          fill=self._lighten(bc, 40), width=2)

        # gloss sheen
        if not pressed:
            sheen = self._lighten(bc, 50)
            pts = [x0+ox+r, y0+oy+1, x1+ox-r, y0+oy+1,
                   x1+ox-r, y0+oy+(y1-y0)//3, x0+ox+r, y0+oy+(y1-y0)//3]
            c.create_polygon(pts, fill=sheen, outline='', stipple='gray25')

        # text + icon
        cx = (x0+ox+x1+ox)//2; cy = (y0+oy+y1+oy)//2
        label = f"{self.icon}  {self.text}" if self.icon else self.text
        tc = self._darken(self.text_color, 20) if pressed else self.text_color
        c.create_text(cx+1, cy+1, text=label, font=self.font,
                      fill=self._darken(bc, 50), anchor='center')
        c.create_text(cx, cy, text=label, font=self.font, fill=tc, anchor='center')

    def _bind(self):
        self.canvas.bind('<Enter>',           self._on_enter)
        self.canvas.bind('<Leave>',           self._on_leave)
        self.canvas.bind('<ButtonPress-1>',   self._on_press)
        self.canvas.bind('<ButtonRelease-1>', self._on_release)

    def _on_enter(self, e=None):
        if self._disabled: return
        self._hovered = True; self._draw()

    def _on_leave(self, e=None):
        self._hovered = False; self._pressed = False; self._draw()

    def _on_press(self, e=None):
        if self._disabled: return
        self._pressed = True; self._draw()

    def _on_release(self, e=None):
        if self._disabled: return
        was = self._pressed
        self._pressed = False; self._hovered = True; self._draw()
        if was and self.command:
            try: self.command()
            except Exception: pass

    def config(self, **kw):
        if 'state' in kw:
            if kw['state'] == 'disabled':
                self._disabled = True; self.canvas.config(cursor='arrow')
                self._save_base = self.base_color; self._save_text = self.text_color
                self.base_color = '#6b7280'; self.text_color = '#d1d5db'; self._draw()
            else:
                self._disabled = False; self.canvas.config(cursor='hand2')
                if hasattr(self, '_save_base'):
                    self.base_color = self._save_base; self.text_color = self._save_text
                self._draw()
        if 'text' in kw: self.text = kw['text']; self._draw()
        if 'bg'   in kw: self.canvas.config(bg=kw['bg'])
        if 'base_color' in kw: self.base_color = kw['base_color']; self._draw()


# ============================================================
#  GLASSMORPHISM CARD
# ============================================================

class GlassCard:
    """Simulated glassmorphism panel."""

    def __init__(self, parent, width, height,
                 tint_color='#6366f1', tint_alpha=0.12,
                 border_color='#ffffff', corner_radius=16, bg_color='#161b22'):
        self.width = width; self.height = height
        self.cr = corner_radius; self.bg = bg_color
        self._canvas = tk.Canvas(parent, width=width, height=height,
                                 highlightthickness=0, bg=bg_color)
        self._draw_glass(tint_color, tint_alpha, border_color)
        self.inner = tk.Frame(self._canvas,
                              bg=self._mix(bg_color, tint_color, tint_alpha))

    def _h2r(self, h):
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

    def _r2h(self, r, g, b):
        return f'#{int(max(0,min(255,r))):02x}{int(max(0,min(255,g))):02x}{int(max(0,min(255,b))):02x}'

    def _mix(self, base, tint, alpha):
        r1,g1,b1 = self._h2r(base); r2,g2,b2 = self._h2r(tint)
        return self._r2h(r1+(r2-r1)*alpha, g1+(g2-g1)*alpha, b1+(b2-b1)*alpha)

    def _rrect(self, x0, y0, x1, y1, r, **kw):
        pts = [x0+r,y0, x1-r,y0, x1,y0, x1,y0+r,
               x1,y1-r, x1,y1, x1-r,y1, x0+r,y1,
               x0,y1, x0,y1-r, x0,y0+r, x0,y0]
        return self._canvas.create_polygon(pts, smooth=True, **kw)

    def _draw_glass(self, tint, alpha, border):
        c = self._canvas; w, h = self.width, self.height; r = self.cr; bg = self.bg
        for i in range(8, 0, -1):
            col = self._mix(bg, '#000000', 0.05*i)
            self._rrect(i, i, w+i, h+i, r+i, fill=col, outline='')
        self._rrect(0, 0, w, h, r, fill=self._mix(bg, tint, alpha), outline='')
        sheen = self._mix(bg, '#ffffff', 0.10)
        c.create_polygon([r, 0, w-r, 0, w//2, h//4, r//2, h//4],
                         smooth=True, fill=sheen, outline='')
        self._rrect(0, 0, w, h, r,
                    fill='', outline=self._mix(bg, '#ffffff', 0.22), width=1)
        self._rrect(1, 1, w-1, h-1, r-1,
                    fill='', outline=self._mix(bg, tint, 0.4), width=1)

    def pack(self, **kw):  self._canvas.pack(**kw)
    def grid(self, **kw):  self._canvas.grid(**kw)
    def place(self, **kw): self._canvas.place(**kw)

    def get_inner(self):
        pad = self.cr
        self._canvas.create_window(pad, pad, anchor='nw', window=self.inner,
                                   width=self.width-pad*2, height=self.height-pad*2)
        return self.inner