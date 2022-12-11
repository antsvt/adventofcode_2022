with open("input.txt") as f:
    lines = f.readlines()

def get_min_max(elf):
    val = elf.split('-')
    return int(val[0]), int(val[1])

def is_2_inside_1(elf1, elf2):
    return elf1[0] <= elf2[0] and elf1[1] >= elf2[1]

def check_pair(elf1, elf2):
    elf1_val = get_min_max(elf1)
    elf2_val = get_min_max(elf2)
    if is_2_inside_1(elf1_val, elf2_val):
        return True
    return is_2_inside_1(elf2_val, elf1_val)

total = 0
for l in lines:
    l = l.strip()
    pairs = l.split(',')
    total += check_pair(pairs[0], pairs[1])

print(total)