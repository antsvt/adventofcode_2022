import math

with open("input.txt") as f:
    lines = f.readlines()

ticks = [20, 60, 100, 140, 180, 220, 1000]
total = 0
commands_counter = 0
registry_value = 1
ticks_counter = 0

for line in lines:
    commands = line.strip().split()
    if commands[0] == 'noop':
        commands_counter += 1
    if commands[0] == 'addx':
        commands_counter += 2

    if commands_counter >= ticks[ticks_counter]:
        total += ticks[ticks_counter] * registry_value
        ticks_counter += 1

    if commands[0] == 'addx':
        registry_value += int(commands[1])
        
print(total)
