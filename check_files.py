import tokenize, io

# Find all triple-quote positions and their line numbers in mouse_manager.py  
with open('src/mouse_manager.py', 'rb') as f:
    content = f.read()

lines = content.split(b'\n')
triple = b'"""'
pos = 0
count = 0
positions = []
while True:
    idx = content.find(triple, pos)
    if idx == -1:
        break
    line_num = content[:idx].count(b'\n') + 1
    positions.append((line_num, idx))
    pos = idx + 3
    count += 1

print(f"Total triple-quotes: {count}")
for i, (ln, p) in enumerate(positions):
    role = "OPEN" if i%2==0 else "CLOSE"
    print(f"  #{i+1} {role} at line {ln}: ...{repr(content[p-5:p+20])}...")
