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

    i += 1
    words = lines[i].strip().split()
    monkey.throw_to_true = int(words[5])

    i += 1
    words = lines[i].strip().split()
    monkey.throw_to_false = int(words[5])

    i += 2
    monkeys.append(monkey)
        
stats = [0 for i in range(len(monkeys))]

for X in range(20):
    for i in range(len(monkeys)):
        print(f'Monkey {i}:')
        m = monkeys[i]
        while m.items:
            stats[i] += 1
            item = m.items[0]
            del m.items[0]
            print(f'  Monkey inspects an item with a worry level of {item}')
            worry_level = (item**m.operation_degree)*m.operation_mult + m.operation_add
            print(f'    Worry level is {worry_level}')
            worry_level = worry_level // 3
            print(f'    Monkey gets bored with item. Worry level is divided by 3 to {worry_level}')
            if worry_level % m.test_divisible == 0:
                print(f'    Current worry level is divisible by {m.test_divisible}')
                print(f'    Item with worry level {worry_level} is thrown to monkey {m.throw_to_true}')
                monkeys[m.throw_to_true].items.append(worry_level)
            else:
                print(f'    Current worry level is not divisible by {m.test_divisible}')
                print(f'    Item with worry level {worry_level} is thrown to monkey {m.throw_to_false}')
                monkeys[m.throw_to_false].items.append(worry_level)
        
stats.sort(reverse=True)
print(stats[0]*stats[1])