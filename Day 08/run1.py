with open("input.txt") as f:
    lines = f.readlines()

grid = []
z_grid = []
for line in lines:
    line = line.strip()
    grid.append(line)
    z_line = []
    for i in line:
        z_line.append(0)
    z_grid.append(z_line)

for i in range(len(grid)):
    max_before = grid[i][0]
    z_grid[i][0] = 1
    for j in range(len(grid[i])):
        if grid[i][j] > max_before:
            z_grid[i][j] = 1
            max_before = grid[i][j]

for i in range(len(grid)):
    max_before = grid[i][-1]
    z_grid[i][-1] = 1
    for j in range(len(grid[i])):
        if grid[i][-j-1] > max_before:
            z_grid[i][-j-1] = 1
            max_before = grid[i][-j-1]

for j in range(len(grid[0])):
    max_before = grid[0][j]
    z_grid[0][j] = 1
    for i in range(len(grid)):
        if grid[i][j] > max_before:
            z_grid[i][j] = 1
            max_before = grid[i][j]

for j in range(len(grid[0])):
    max_before = grid[-1][j]
    z_grid[-1][j] = 1
    for i in range(len(grid)):
        if grid[-i-1][j] > max_before:
            z_grid[-i-1][j] = 1
            max_before = grid[-i-1][j]

ssum = 0
for line in z_grid:
    ssum += sum(line)
print(ssum)

