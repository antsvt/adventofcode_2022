with open("input.txt") as f:
    lines = f.readlines()

moves = False

stapel = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}

def push_line(line):
    for i in range(9):
        symbol = line[1+4*i]
        if symbol != ' ':
            stapel[i].insert(0, symbol)
    pass

def do_move(line):
    line = line.strip().split()
    if len(line) < 6:
        return

    how_much = int(line[1])
    from_where = int(line[3])
    to_where = int(line[5])

    for i in range(how_much):
        stapel[to_where - 1].append(stapel[from_where - 1][-1])
        del stapel[from_where - 1][-1]

    pass

for line in lines:
    if not moves:
        if line[1] != '1':
            push_line(line)
        else:
            moves = True
    else:
        do_move(line)

for i in stapel.keys():
    print(stapel[i][-1])