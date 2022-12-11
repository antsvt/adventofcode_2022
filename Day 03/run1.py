with open("input.txt") as f:
    lines = f.readlines()

def get_priority(s):
    os = ord(s)
    if os >= ord('a') and os <= ord('z'):
        return ord(s) - ord('a') + 1
    return ord(s) - ord('A') + 27

total = 0
for l in lines:
    l = l.strip()
    sl1 = l[:len(l)//2]
    sl2 = l[len(l)//2:]
    for s in sl2:
        if s in sl1:
            total += get_priority(s)
            break

print(total)