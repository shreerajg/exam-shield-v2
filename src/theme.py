import tkinter as tk
from tkinter import ttk
import sys
import os

class ExamShieldTheme:
    """Modern theme system for Exam Shield Pro"""
    
    def __init__(self, theme_mode="light"):
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
        """Light theme color palette"""
        return {
            # Primary colors
            'primary': '#2563EB',
            'primary_light': '#60A5FA',
            'primary_dark': '#1D4ED8',
            'primary_hover': '#1E40AF',
            
            # Secondary colors
            'secondary': '#10B981',
            'secondary_light': '#34D399',
            'secondary_dark': '#047857',
            
            # Status colors
            'success': '#10B981',
            'warning': '#F59E0B',
            'danger': '#EF4444',
            'info': '#3B82F6',
            
            # Neutral colors
            'white': '#FFFFFF',
            'gray_50': '#F9FAFB',
            'gray_100': '#F3F4F6',
            'gray_200': '#E5E7EB',
            'gray_300': '#D1D5DB',
            'gray_400': '#9CA3AF',
            'gray_500': '#6B7280',
            'gray_600': '#4B5563',
            'gray_700': '#374151',
            'gray_800': '#1F2937',
            'gray_900': '#111827',
            
            # Surface colors
            'background': '#F8FAFC',
            'surface': '#FFFFFF',
            'card': '#FFFFFF',
            'sidebar': '#1E293B',
            'sidebar_hover': '#334155',
            
            # Text colors
            'text_primary': '#1E293B',
            'text_secondary': '#64748B',
            'text_muted': '#94A3B8',
            'text_inverse': '#FFFFFF',
            
            # Border colors
            'border': '#E2E8F0',
            'border_light': '#F1F5F9',
            'border_focus': '#2563EB',
            
            # Shadow colors
            'shadow': 'rgba(0, 0, 0, 0.1)',
            'shadow_dark': 'rgba(0, 0, 0, 0.25)',
        }
    
    def get_dark_theme(self):
        """Dark theme color palette"""
        return {
            # Primary colors (same as light)
            'primary': '#3B82F6',
            'primary_light': '#60A5FA',
            'primary_dark': '#1D4ED8',
            'primary_hover': '#2563EB',
            
            # Secondary colors
            'secondary': '#10B981',
            'secondary_light': '#34D399',
            'secondary_dark': '#047857',
            
            # Status colors
            'success': '#10B981',
            'warning': '#F59E0B',
            'danger': '#EF4444',
            'info': '#3B82F6',
            
            # Neutral colors (inverted)
            'white': '#FFFFFF',
            'gray_50': '#18181B',
            'gray_100': '#27272A',
            'gray_200': '#3F3F46',
            'gray_300': '#52525B',
            'gray_400': '#71717A',
            'gray_500': '#A1A1AA',
            'gray_600': '#D4D4D8',
            'gray_700': '#E4E4E7',
            'gray_800': '#F4F4F5',
            'gray_900': '#FAFAFA',
            
            # Surface colors
            'background': '#0F172A',
            'surface': '#1E293B',
            'card': '#1E293B',
            'sidebar': '#0F172A',
            'sidebar_hover': '#1E293B',
            
            # Text colors
            'text_primary': '#F1F5F9',
            'text_secondary': '#CBD5E1',
            'text_muted': '#94A3B8',
            'text_inverse': '#1E293B',
            
            # Border colors
            'border': '#334155',
            'border_light': '#475569',
            'border_focus': '#3B82F6',
            
            # Shadow colors
            'shadow': 'rgba(0, 0, 0, 0.3)',
            'shadow_dark': 'rgba(0, 0, 0, 0.5)',
        }
    
    def get_pink_theme(self):
        """Pink theme color palette"""
        return {
            # Primary colors
            'primary': '#EC4899',
            'primary_light': '#F472B6',
            'primary_dark': '#BE185D',
            'primary_hover': '#DB2777',
            
            # Secondary colors
            'secondary': '#8B5CF6',
            'secondary_light': '#A78BFA',
            'secondary_dark': '#6D28D9',
            
            # Status colors
            'success': '#10B981',
            'warning': '#F59E0B',
            'danger': '#EF4444',
            'info': '#3B82F6',
            
            # Neutral colors
            'white': '#FFFFFF',
            'gray_50': '#FDF2F8',
            'gray_100': '#FCE7F3',
            'gray_200': '#FBCFE8',
            'gray_300': '#F9A8D4',
            'gray_400': '#F472B6',
            'gray_500': '#EC4899',
            'gray_600': '#DB2777',
            'gray_700': '#BE185D',
            'gray_800': '#9D174D',
            'gray_900': '#831843',
            
            # Surface colors
            'background': '#FDF2F8',
            'surface': '#FFFFFF',
            'card': '#FFFFFF',
            'sidebar': '#831843',
            'sidebar_hover': '#9D174D',
            
            # Text colors
            'text_primary': '#831843',
            'text_secondary': '#DB2777',
            'text_muted': '#F472B6',
            'text_inverse': '#FFFFFF',
            
            # Border colors
            'border': '#FBCFE8',
            'border_light': '#FCE7F3',
            'border_focus': '#EC4899',
            
            # Shadow colors
            'shadow': 'rgba(236, 72, 153, 0.1)',
            'shadow_dark': 'rgba(236, 72, 153, 0.25)',
        }
    
    def get_font_system(self):
        """Professional font system"""
        # Detect system fonts
        system_font = self.get_system_font()
        
        return {
            'heading': (system_font, 28, 'bold'),
            'title': (system_font, 20, 'bold'),
            'subtitle': (system_font, 16, 'bold'),
            'body': (system_font, 11, 'normal'),
            'body_bold': (system_font, 11, 'bold'),
            'body_large': (system_font, 12, 'normal'),
            'caption': (system_font, 10, 'normal'),
            'small': (system_font, 9, 'normal'),
            'mono': ('Consolas', 10, 'normal'),
            'mono_small': ('Consolas', 9, 'normal'),
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
        # Primary button
        style.configure('Primary.TButton',
                       background=self.colors['primary'],
                       foreground=self.colors['text_inverse'],
                       font=self.fonts['body_bold'],
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat')
        
        style.map('Primary.TButton',
                 background=[('active', self.colors['primary_hover']),
                           ('pressed', self.colors['primary_dark'])])
        
        # Success button
        style.configure('Success.TButton',
                       background=self.colors['success'],
                       foreground=self.colors['text_inverse'],
                       font=self.fonts['body_bold'],
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat')
        
        # Danger button
        style.configure('Danger.TButton',
                       background=self.colors['danger'],
                       foreground=self.colors['text_inverse'],
                       font=self.fonts['body_bold'],
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat')
        
        # Warning button
        style.configure('Warning.TButton',
                       background=self.colors['warning'],
                       foreground=self.colors['text_inverse'],
                       font=self.fonts['body_bold'],
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat')
    
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
    'dark': ExamShieldTheme('dark'),
    'pink': ExamShieldTheme('pink'),
}

def get_theme(theme_name='light'):
    """Get theme instance"""
    return THEMES.get(theme_name, THEMES['light'])