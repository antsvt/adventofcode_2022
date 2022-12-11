with open("input.txt") as f:
    lines = f.readlines()

def get_min_max(elf):
    val = elf.split('-')
    return int(val[0]), int(val[1])

def is_overlap(elf1, elf2):
    overlap1 = elf1[0] <= elf2[0] and elf1[1] >= elf2[0]
    overlap2 = elf2[0] <= elf1[0] and elf2[1] >= elf1[0]
    return overlap1 or overlap2

def check_pair(elf1, elf2):
    elf1_val = get_min_max(elf1)
    elf2_val = get_min_max(elf2)
    return is_overlap(elf2_val, elf1_val)

total = 0
for l in lines:
    l = l.strip()
    pairs = l.split(',')
    total += check_pair(pairs[0], pairs[1])

print(total)