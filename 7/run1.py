with open("input.txt") as f:
    lines = f.readlines()

tree = {"/":{}}
path = ["/"]

def add_dir(name):
    global path
    global tree

    current = tree
    for p in path:
        current = current[p]
    current[name] = {}
    pass

def add_file(name, size):
    global path
    global tree

    current = tree
    for p in path:
        current = current[p]
    current[name] = size

def change_dir(where):
    global path

    if where == "/":
        path = ["/"]
    elif where == "..":
        path = path[:-1]
    else:
        path.append(where)

for line in lines:
    line = line.strip()
    words = line.split()
    if words[0] == "$":
        if words[1] == "cd":
            change_dir(words[2])
    elif words[0] == "dir":
        add_dir(words[1])
    else:
        add_file(words[1], int(words[0]))


dirs = {}

def get_subdir_size(name, subtree):
    global dirs

    total = 0
    for i in subtree.keys():
        if isinstance(subtree[i], int):
            total += subtree[i]
        else:
            total += get_subdir_size(name + "/" + i, subtree[i])
    if name in dirs:
        dirs[name] = total
    else:
        dirs[name] = total
    return total

used = get_subdir_size("/", tree["/"])

total = 0
for i in dirs.keys():
    if dirs[i] <= 100000:
        total += dirs[i]

print(total)