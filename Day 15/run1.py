import math

with open("input.txt") as f:
    lines = f.readlines()

y_num = 2000000
#y_num = 10
not_a_beacon = []
beacons = []

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def calculate_for_line(sensor_x, sensor_y, beacon_x, beacon_y):
    global not_a_beacon
    manh_dist = dist(sensor_x, sensor_y, beacon_x, beacon_y)

    diff = manh_dist - dist(sensor_x, sensor_y, sensor_x, 0) 
    if diff < 0:
        return

    not_a_beacon.append([sensor_x - diff, sensor_x + diff])

for line in lines:
    line = line.strip().split('=')
    s_x = int(line[1].split(',')[0])
    s_y = int(line[2].split(':')[0]) - y_num
    b_x = int(line[3].split(',')[0])
    b_y = int(line[4]) - y_num
    
    if b_y == 0 and b_x not in beacons:
        beacons.append(b_x)

    calculate_for_line(s_x, s_y, b_x, b_y)

not_a_beacon.sort(key=lambda x: x[0])
beacons.sort()

last = not_a_beacon[0].copy()
merged = []
for interval in not_a_beacon:
    if interval[0] <= last[1]:
        last[1] = max([last[1], interval[1]])
    else:
        merged.append(last)
        last = interval.copy()

merged.append(last)

print(not_a_beacon)
print(merged)
print(beacons)

not_a_beacon = merged

count = 0
b_ind = 0
for interval in not_a_beacon:
    count += interval[1] - interval[0] + 1

    while b_ind < len(beacons) and interval[0] <= beacons[b_ind] and beacons[b_ind] <= interval[1]:
        count -= 1
        b_ind += 1  

print(count)