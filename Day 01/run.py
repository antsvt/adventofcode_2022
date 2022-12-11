with open("input.txt") as f:
    lines = f.readlines();

calories = []
current = 0
for l in lines:
    l = l.strip()
    if l == "":
        calories.append(current)
        current = 0
    else:
        current += int(l)

calories.append(current)
calories.sort(reverse=True)

print(calories[0] + calories[1] + calories[2])
