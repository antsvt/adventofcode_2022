with open("input.txt") as f:
    lines = f.readlines()

marker = ""

line = lines[0].strip()
counter = 0

for symb in line:
    counter += 1
    while symb in marker:
        marker = marker.lstrip(marker[0])

    marker += symb
    if len(marker) == 14:
        break

print(counter)