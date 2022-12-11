with open("input.txt") as f:
    lines = f.readlines()

grid = []
for line in lines:
    line = line.strip()
    grid.append(line)

def fix_counter(c):
    if c == 0:
        return 1
    return c

def get_vis(i, j):
    global grid
    counter = 0
    value = grid[i][j]
    for x in range(i-1, -1, -1):
        counter += 1
        if grid[x][j] >= value:
            break
    total = fix_counter(counter)
    counter = 0
    for x in range(i+1, len(grid)):
        counter += 1
        if grid[x][j] >= value:
            break
    total *= fix_counter(counter)
    counter = 0
    for y in range(j-1, -1, -1):
        counter += 1
        if grid[i][y] >= value:
            break
    total *= fix_counter(counter)
    counter = 0
    for y in range(j+1, len(grid[i])):
        counter += 1
        if grid[i][y] >= value:
            break
    total *= fix_counter(counter)

    return total

max_val = 0
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        val = get_vis(i, j)
        if val > max_val:
            max_val = val

print(max_val)