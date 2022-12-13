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

i = 0
index = 0
total = 0
while i < len(lines):
    index += 1
    line1 = lines[i]
    i += 1
    line2 = lines[i]
    i += 2

    line1 = "line1 = " + line1
    line2 = "line2 = " + line2

    exec(line1)
    exec(line2)
    if is_it_right_order(line1, line2)[0]:
        total += index

print(total)