"""
Helper script to resolve git merge conflicts by keeping the HEAD side.
Run this from the project root directory.
"""
import os
import re

def resolve_conflict_keep_head(content):
    """Strip conflict markers, keep HEAD (<<<) side, discard ours (>>>) side."""
    lines = content.split('\n')
    result = []
    in_head = False
    in_theirs = False
    
    for line in lines:
        if line.startswith('<<<<<<< HEAD'):
            in_head = True
            in_theirs = False
            continue
        elif line.startswith('======='):
            if in_head:
                in_head = False
                in_theirs = True
            continue
        elif line.startswith('>>>>>>> '):
            in_theirs = False
            in_head = False
            continue
        
        if in_theirs:
            continue  # Skip the "theirs" side
        
        result.append(line)
    
    return '\n'.join(result)

# Files to resolve
files_to_resolve = [
    'main.py',
    'config.py',
    'admin_panel.py',
    'security_manager.py',
    'mouse_manager.py',
    'system_tray.py',
    'window_manager.py',
]

project_root = os.path.dirname(os.path.abspath(__file__))

for fname in files_to_resolve:
    fpath = os.path.join(project_root, fname)
    if not os.path.exists(fpath):
        print(f"SKIP (not found): {fname}")
        continue
    
    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    if '<<<<<<< HEAD' not in content:
        print(f"OK (no conflicts): {fname}")
        continue
    
    resolved = resolve_conflict_keep_head(content)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(resolved)
    
    print(f"RESOLVED: {fname}")

print("\nAll done!")
