"""
Enhanced Configuration for Exam Shield Pro
Premium Security Suite Settings
"""

import os

# Resolve paths relative to the project root (this file's directory)
_ROOT = os.path.dirname(os.path.abspath(__file__))

class Config:
    # Application settings
<<<<<<< HEAD
    APP_NAME = "Exam Shield"
    VERSION = "2.0.0"
    
    # Database settings — stored in data/ subfolder
    DATABASE_NAME = "exam_shield.db"
    DATABASE_PATH = os.path.join(_ROOT, "data", DATABASE_NAME)
=======
    APP_NAME = "Exam Shield Pro"
    VERSION = "2.0.0"
    
    # Database settings
    DATABASE_NAME = "exam_shield_pro.db"
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), DATABASE_NAME)
>>>>>>> 1543317 (adding elements in main page)
    
    # Default admin credentials (used only on first launch)
    DEFAULT_USERNAME = "admin"
    DEFAULT_PASSWORD = "admin"
    # Legacy aliases kept for backward compatibility
    DEFAULT_ADMIN_USERNAME = "admin"
    DEFAULT_ADMIN_PASSWORD = "admin"
    
    # Blocked keys - Enhanced list
    BLOCKED_KEYS = [
        'alt+tab', 'alt+f4', 'win+d', 'win+l', 'win+r',
        'ctrl+alt+del', 'ctrl+shift+esc', 'f11', 'alt+space',
        'win+tab', 'ctrl+alt+t', 'ctrl+shift+i', 'f12',
        'ctrl+u', 'ctrl+shift+j', 'ctrl+shift+c'
    ]
    
    # Blocked mouse buttons
    BLOCKED_MOUSE_BUTTONS = [
        'middle', 'x1', 'x2', 'side', 'back', 'forward'
    ]
    
    # Admin access key
    ADMIN_ACCESS_KEY = 'ctrl+shift+y'
    
    # Individual blocking control flags
    SELECTIVE_BLOCKING = {
        'keyboard': True,
        'mouse': True,
        'internet': True,
        'windows': True,
        'processes': True
    }
    
    # Network blocking settings
    BLOCK_INTERNET = True
    BLOCKED_WEBSITES = [
        'google.com', 'facebook.com', 'youtube.com', 'twitter.com',
        'instagram.com', 'tiktok.com', 'reddit.com', 'discord.com',
        'whatsapp.com', 'telegram.org', 'snapchat.com', 'github.com'
    ]
    
<<<<<<< HEAD
    # Premium UI Colors
    COLORS = {
        'primary': '#1e3d59',      # Deep navy blue
        'secondary': '#17223b',     # Darker navy
        'accent': '#ffc947',       # Premium gold
        'success': '#27ae60',      # Professional green
        'danger': '#e74c3c',       # Professional red
        'warning': '#f39c12',      # Premium orange
        'info': '#3498db',         # Professional blue
        'surface': '#f8f9fa',      # Light surface
        'card': '#ffffff',         # White cards
        'text_primary': '#2c3e50', # Dark text
        'text_secondary': '#7f8c8d', # Gray text
        'border': '#dee2e6',       # Light borders
        'light_blue': '#ecf4ff',   # Very light blue
        'light_green': '#e8f5e8',  # Very light green
        'light_yellow': '#fff8e1', # Very light yellow
        'light_red': '#ffebee'     # Very light red
=======
    # Premium UI Colors - Modern Dark Theme
    COLORS = {
        'primary': '#00D4FF',           # Bright cyan
        'primary_dark': '#0099CC',     # Darker cyan
        'secondary': '#4ADE80',        # Green
        'danger': '#FF4444',           # Red
        'warning': '#FBBF24',          # Amber
        'info': '#60A5FA',             # Blue
        'success': '#10B981',          # Emerald
        
        # Dark theme palette
        'bg_primary': '#0F1419',       # Very dark blue-gray
        'bg_secondary': '#1E2328',     # Dark gray
        'bg_tertiary': '#252A31',      # Medium gray
        'bg_accent': '#2A3138',        # Light gray
        
        # Text colors
        'text_primary': '#FFFFFF',     # White
        'text_secondary': '#E5E7EB',   # Light gray
        'text_muted': '#9CA3AF',       # Gray
        'text_accent': '#00D4FF',      # Cyan accent
        
        # Status colors
        'status_active': '#10B981',    # Green
        'status_inactive': '#6B7280',  # Gray
        'status_danger': '#EF4444',    # Red
        'status_warning': '#F59E0B'    # Orange
    }
    
    # Typography
    FONTS = {
        'primary': ('Segoe UI', 11),
        'heading': ('Segoe UI', 14, 'bold'),
        'title': ('Segoe UI', 18, 'bold'),
        'button': ('Segoe UI', 11, 'bold'),
        'small': ('Segoe UI', 9),
        'code': ('Consolas', 10)
>>>>>>> 1543317 (adding elements in main page)
    }
    
    # Logging settings
    LOG_RETENTION_DAYS = 30
    MAX_LOG_ENTRIES = 10000
    
    # UI Settings
    WINDOW_ANIMATIONS = True
    THEME_MODE = 'dark'
    AUTO_REFRESH_INTERVAL = 2000  # milliseconds
