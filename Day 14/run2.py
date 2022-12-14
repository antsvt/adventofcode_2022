import math

with open("input.txt") as f:
    lines = f.readlines()

borders = []
for line in lines:
    line = line.strip().split(' -> ')
    pairs = []
    for l in line:
        l = l.split(',')
        x = int(l[0])
        y = int(l[1])
        pairs.append((x,y))
    borders.append(pairs)

max_x = borders[0][0][0]
min_x = max_x
max_y = borders[0][0][1]
for b in borders:
    for (x,y) in b:
        max_x = max([max_x, x])
        min_x = min([min_x, x])
        max_y = max([max_y, y])

max_y += 2

min_x -= max_y
max_x += max_y
map = [[0 for i in range(min_x, max_x + 1)] for j in range(max_y + 1)]
for b in borders:
    for i in range(1, len(b)):
        (x1, y1) = b[i - 1]
        (x2, y2) = b[i]

        if x1 != x2:
            for j in range(min([x1, x2]), max([x1, x2])+1):
                map[y1][j-min_x] = 1
        else:
            for j in range(min([y1, y2]), max([y1, y2])+1):
                map[j][x1-min_x] = 1

for i in range(min_x, max_x+1):
    map[max_y][i-min_x] = 1

def draw_map(map):
    for l in map:
        line = ""
        for s in l:
            if s == 0:
                line += '.'
            elif s == 1:
                line += '#'
            else:
                line += 'o'
        print(line)

#draw_map(map)

old_counter = -1
counter = 0
while old_counter != counter:
    x = 500
    y = 0
    old_counter = counter
    while map[0][500 - min_x] == 0:
        if len(map) - 1 <= y:
            break

        if map[y+1][x - min_x] == 0:
            y += 1
            continue

        if x < min_x:
            break

        if map[y+1][x-1 - min_x] == 0:
            y += 1
            x -= 1
            continue

        if x >= max_x:
            break
        
        if map[y+1][x+1 - min_x] == 0:
            y += 1
            x += 1
            continue

        map[y][x - min_x] = 2
        counter += 1
        break

#draw_map(map)

print(counter)