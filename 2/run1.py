with open("input.txt") as f:
    lines = f.readlines()

def get_my_points(my_turn):
    my_turm = my_turn.strip()
    points = {'X':1, 'Y':2, 'Z':3}
    return points[my_turm]
    
def get_win_ponts(turn1, turn2):
    turn1 = turn1.strip()
    turn2 = turn2.strip()
    points = {'A':{'X':3, 'Y':6, 'Z':0}, 
              'B':{'X':0, 'Y':3, 'Z':6},
              'C':{'X':6, 'Y':0, 'Z':3},}
    return points[turn1][turn2]

total = 0
for l in lines:
    l = l.strip().split()
    total += get_my_points(l[1])
    total += get_win_ponts(l[0], l[1])

print(total)
