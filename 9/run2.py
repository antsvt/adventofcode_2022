import math

with open("input.txt") as f:
    lines = f.readlines()

rope=[(1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1)]
visited = [rope[9]]

def move_head(direction):
    global rope
    head = rope[0]
    x = head[0]
    y = head[1]
    if direction == 'U':
        y += 1
    elif direction == 'D':
        y -= 1
    elif direction == 'R':
        x += 1
    elif direction == 'L':
        x -= 1 
    return (x, y)

def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    if x > 0:
        return 1

def move_tail(head, tail):
    x = tail[0]
    y = tail[1]

    if abs(x - head[0]) > 1 or abs(y - head[1]) > 1:
        x += sign(head[0] - x)
        y += sign(head[1] - y)

    return (x, y)

def emulate_move(direction):
    global rope
    rope[0] = move_head(direction)
    for i in range(9):
        rope[i+1] = move_tail(rope[i], rope[i+1])

for line in lines:
    direction, how_far = line.strip().split()
    how_far = int(how_far)
    for i in range(how_far):
        emulate_move(direction)
        if rope[9] not in visited:
            visited.append(rope[9])

print(len(visited))
