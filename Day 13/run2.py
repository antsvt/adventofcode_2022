import math

with open("input.txt") as f:
    lines = f.readlines()

def is_it_right_order(left, right):
    if type(left) is int and type(right) is int:
        return (left < right, left > right)

    if type(left) is int:
        left = [left]
    if type(right) is int:
        right = [right]

    for elem in zip(left, right):
        res = is_it_right_order(elem[0], elem[1])
        if res[0] or res[1]:
            return res

    return (len(left) < len(right), len(left) > len(right))

def cmp(left, right):
    res = is_it_right_order(left, right)
    if not res[0] and not res[1]:
        return 0
    if res[0]:
        return -1
    return 1

packets = []
i = 0
while i < len(lines):
    line1 = lines[i]
    i += 1
    line2 = lines[i]
    i += 2

    line1 = "line1 = " + line1
    line2 = "line2 = " + line2

    exec(line1)
    exec(line2)
    packets.append(line1)
    packets.append(line2)

packets.append([[2]])
packets.append([[6]])

import functools
packets.sort(key=functools.cmp_to_key(cmp), reverse=False)

total = 1
i = 0
for p in packets:
    i += 1
    #print(p)
    if p == [[2]] or p == [[6]]:
        total *= i

print(total)