with open("input.txt") as f:
    lines = f.readlines()

def get_priority(s):
    os = ord(s)
    if os >= ord('a') and os <= ord('z'):
        return ord(s) - ord('a') + 1
    return ord(s) - ord('A') + 27

def get_dublicates(l1, l2):
    res = ""
    for s in l2:
        if s in l1:
            res += s
    return res


total = 0
groups = len(lines)//3
for counter in range(groups):
    l1 = lines[3*counter].strip()
    l2 =  lines[3*counter + 1].strip()
    l3 =  lines[3*counter + 2].strip()

    total += get_priority(get_dublicates(get_dublicates(l1, l2), l3)[0])

print(total)