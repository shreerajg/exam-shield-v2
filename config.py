"""
Configuration settings for Exam Shield
"""
<<<<<<< HEAD

=======
>>>>>>> 8516873 (Initial commit: Project version 1)
import os

class Config:
    # Application settings
    APP_NAME = "Exam Shield"
    VERSION = "1.1.0"
    
    # Database settings
    DATABASE_NAME = "exam_shield.db"
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), DATABASE_NAME)
    
<<<<<<< HEAD
    # Security settings - KEEPING ORIGINAL NAMES
=======
    # Security settings
>>>>>>> 8516873 (Initial commit: Project version 1)
    DEFAULT_ADMIN_USERNAME = "admin"
    DEFAULT_ADMIN_PASSWORD = "admin"
    
    # Blocked keys
    BLOCKED_KEYS = [
        'alt+tab', 'alt+f4', 'win+d', 'win+l', 'win+r',
        'ctrl+alt+del', 'ctrl+shift+esc', 'f11', 'alt+space',
        'win+tab', 'ctrl+alt+t'
    ]
    
    # Blocked mouse buttons
    BLOCKED_MOUSE_BUTTONS = [
        'middle', 'x1', 'x2', 'side'
    ]
    
<<<<<<< HEAD
    # Admin access key
    ADMIN_ACCESS_KEY = 'ctrl+shift+y'
    
    # Individual blocking control flags
=======
    # FIXED: Changed admin access key to Ctrl+Shift+Y
    ADMIN_ACCESS_KEY = 'ctrl+shift+y'
    
    # NEW: Individual blocking control flags
>>>>>>> 8516873 (Initial commit: Project version 1)
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
        'instagram.com', 'tiktok.com', 'reddit.com', 'discord.com'
    ]
    
<<<<<<< HEAD
    # Premium UI Colors - UPDATED FOR PREMIUM LOOK
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
    # UI Colors
    COLORS = {
        'primary': '#2196F3',
        'secondary': '#FFC107',
        'success': '#4CAF50',
        'danger': '#F44336',
        'warning': '#FF9800',
        'info': '#00BCD4',
        'light': '#F5F5F5',
        'dark': '#212121'
>>>>>>> 8516873 (Initial commit: Project version 1)
    }
    
    # Logging settings
    LOG_RETENTION_DAYS = 30
    MAX_LOG_ENTRIES = 10000
