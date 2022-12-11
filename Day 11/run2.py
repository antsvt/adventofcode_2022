import math

with open("input.txt") as f:
    lines = f.readlines()

class Monkey:
    test_divisible = 1
    operation_mult = 1
    operation_degree = 1
    operation_add = 0
    throw_to_true = 0
    throw_to_false = 0
    items = []
    
monkeys = []
i = 0
worry_div_max = 1

while i < len(lines):
    monkey = Monkey()

    i += 1
    line = lines[i]
    monkey.items = [ int(x.split(',')[0]) for x in line.strip().split()[2:] ]

    i += 1
    words = lines[i].strip().split()
    if words[5] == 'old':
        monkey.operation_degree = 2
    elif words[4] == '*':
        monkey.operation_mult = int(words[5])
    else:
        monkey.operation_add = int(words[5])

    i += 1
    words = lines[i].strip().split()
    monkey.test_divisible = int(words[3])
    if worry_div_max % monkey.test_divisible != 0:
        worry_div_max *= monkey.test_divisible

    i += 1
    words = lines[i].strip().split()
    monkey.throw_to_true = int(words[5])

    i += 1
    words = lines[i].strip().split()
    monkey.throw_to_false = int(words[5])

    i += 2
    monkeys.append(monkey)
        
stats = [0 for i in range(len(monkeys))]
print_stats = [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

for X in range(10000):
    for i in range(len(monkeys)):
        m = monkeys[i]
        while m.items:
            stats[i] += 1
            item = m.items[0]
            del m.items[0]
            worry_level = (item**m.operation_degree)*m.operation_mult + m.operation_add
            worry_level = worry_level % worry_div_max
            if worry_level % m.test_divisible == 0:
                monkeys[m.throw_to_true].items.append(worry_level)
            else:
                monkeys[m.throw_to_false].items.append(worry_level)

    if X+1 in print_stats:
        print(f'== After round {X} ==')
        for j in range(len(stats)):
            print(f'Monkey {j} inspected items {stats[j]} times.')
        print()
        
stats.sort(reverse=True)
print(stats[0]*stats[1])