import math

with open("input.txt") as f:
    lines = f.readlines()

value = 1
values = []

for line in lines:
    commands = line.strip().split()
    if commands[0] == 'noop':
        values.append(value)
    if commands[0] == 'addx':
        values.append(value)
        values.append(value)
        value += int(commands[1])

for i in range(240):
    if i%40 == 0:
        print()
    pos = i%40 + 1
    if values[i] <= pos and values[i] + 2 >= pos:
        print('#', end='')
    else: 
        print('.', end='')
