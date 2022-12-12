import math

with open("input.txt") as f:
    lines = f.readlines()

map = []
visited = []
y = 0
starts = []
m_end = (0, 0)

for line in lines:
    line = line.strip()
    x = 0
    row = []
    for s in line:
        if s == 'S':
            m_start = (x, y)
            s = 'a'
        elif s == 'E':
            m_end = (x, y)
            s = 'z'
        if s == 'a':
            starts.append((x,y))
        row.append(ord(s) - ord('a'))
        x += 1
    map.append(row)
    y += 1

class Postion:
    def __init__(self, x, y, counter):
        self.x = x
        self.y = y
        self.counter = counter

def add_to_map(x, y, high, counter, visited):
    global m_end
    global map

    if x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
        return False
    if visited[y][x] >= 0:
        return False
    if map[y][x] > high + 1:
        return False
    if x == m_end[0] and y == m_end[1]:
        print(counter + 1)
        return True

    visited[y][x] = counter + 1
    pos = Postion(x, y, counter + 1)
    positions.append(pos)
    return False

for start in starts:
    visited = [[-1 for j in i] for i in map]
    visited[start[1]][start[0]] = 0

    positions = []
    pos = Postion(start[0], start[1], 0)
    positions.append(pos)

    while len(positions) > 0:
        p = positions[0]
        del positions[0]
        hight = map[p.y][p.x]

        if  add_to_map(p.x - 1, p.y, hight, p.counter, visited):
            break
        if  add_to_map(p.x + 1, p.y, hight, p.counter, visited):
            break
        if  add_to_map(p.x, p.y - 1, hight, p.counter, visited):
            break
        if  add_to_map(p.x, p.y + 1, hight, p.counter, visited):
            break

print(1)