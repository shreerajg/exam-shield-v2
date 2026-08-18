import tokenize, io

for fname in ['src/mouse_manager.py', 'src/system_tray.py']:
    try:
        with open(fname, 'rb') as f:
            content = f.read()
        # Count triple double quotes
        count = content.count(b'"""')
        print(f"{fname}: triple-quotes={count}, even={count%2==0}")
        # Try tokenizing
        try:
            list(tokenize.tokenize(io.BytesIO(content).readline))
            print(f"  Tokenize OK")
        except tokenize.TokenError as e:
            print(f"  TokenError: {e}")
    except Exception as e:
        print(f"  Error reading: {e}")

# Also check system_tray lines 1-15 raw
print("\n--- system_tray.py lines 1-15 raw ---")
with open('src/system_tray.py', 'rb') as f:
    content = f.read()
lines = content.split(b'\n')
for i, line in enumerate(lines[:15], 1):
    print(f"{i}: {repr(line)}")
