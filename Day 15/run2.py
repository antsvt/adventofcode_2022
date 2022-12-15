import math

max_val = 4000000   #20

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def calculate_for_line(data, sensor_x, sensor_y, beacon_x, beacon_y):
    manh_dist = dist(sensor_x, sensor_y, beacon_x, beacon_y)

    diff = manh_dist - dist(sensor_x, sensor_y, sensor_x, 0) 
    if diff < 0:
        return

    data.append([sensor_x - diff, sensor_x + diff])

def merge(to_merge):
    last = to_merge[0].copy()
    merged = []
    for interval in to_merge:
        if interval[0] <= last[1]:
            last[1] = max([last[1], interval[1]])
        else:
            if last[1] >= 0 and last[0] <= max_val:
                merged.append(last)
            last = interval.copy()

    if last[1] >= 0 and last[0] <= max_val:
        merged.append(last)
    return merged

def find_for_line(num):
    not_a_beacon = []
    with open("input.txt") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip().split('=')
        s_x = int(line[1].split(',')[0])
        s_y = int(line[2].split(':')[0]) - num
        b_x = int(line[3].split(',')[0])
        b_y = int(line[4]) - num

        calculate_for_line(not_a_beacon, s_x, s_y, b_x, b_y)

    not_a_beacon.sort(key=lambda x: x[0])
    not_a_beacon = merge(not_a_beacon)
    if not_a_beacon[0][0] > 0:
        return not_a_beacon[0][0]-1
    if not_a_beacon[-1][1] < max_val:
        return not_a_beacon[-1][1]+1
    if len(not_a_beacon) > 1:
        return not_a_beacon[0][1]+1
    return -1

for i in range(max_val + 1):
    val = find_for_line(i)
    if val > 0:
        print(val, i)
        print(val*4000000 + i)
        break