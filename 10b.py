import math
import time
import shapely.geometry as geo

timings = []
def timestamp(milestone):
    timings.append((milestone,time.time()))
    return

def runtimes():
    if len(timings) < 2:
        out = "At least two events needed for timings."
    else:
        out = ""
        for n in range(1,len(timings)):
            out += "From '" + timings[n-1][0] + "' to '" + timings[n][0] + "': " + duration(timings[n][1] - timings[n-1][1]) + '\n'
    return out

def duration(interval):
    hours = math.floor(interval / 3600)
    remaining = interval - hours * 3600
    mins = math.floor(remaining / 60)
    remaining = remaining - mins * 60
    secs = remaining

    out = ""
    if hours > 0:
        out = str(hours) + " hours"
    if mins > 0:
        if out != "":
            out += ", "
        out += str(mins) + " minutes"
    if secs > 0:
        if out != "":
            out += ", "
        out += str(secs) + " seconds"
    return out

timestamp('start')

datafile = "../../AoC/2023/10testb.txt"

NORTH = 0b0001
SOUTH = 0b0010
EAST = 0b0100
WEST = 0b1000
GROUND = 0
START = -1

directions = {NORTH: [0, -1, SOUTH],
              SOUTH: [0, 1, NORTH],
              EAST: [1, 0, WEST],
              WEST: [-1, 0, EAST]}

# convert symbols to bits
sym_bin = {'|': NORTH | SOUTH,
           '-': EAST | WEST,
           'L': NORTH | EAST,
           'J': NORTH | WEST,
           '7': SOUTH | WEST,
           'F': SOUTH | EAST,
           '.': GROUND,
           'S': START}

locs = []
points = []

with open(datafile) as input:
    for line in input:
        locs.append([sym_bin[x] for x in line[:-1]])
    
# find start
found_start = False
for y in range(len(locs)):
    for x in range(len(locs[y])):
        if locs[y][x] == START:
            start_coords = (x,y)
            found_start = True
            break
    if found_start:
        break

points.append(start_coords)

for dir in directions.values():
    coords = (start_coords[0]+dir[0], start_coords[1]+dir[1])
    if coords[0] >= 0 and coords[0] < len(locs[0]) and coords[1] >= 0 and coords[1] < len(locs):
        if locs[coords[1]][coords[0]] & dir[2] != 0:
            break

while locs[coords[1]][coords[0]] != START:
    points.append((coords))
    dir = directions[locs[coords[1]][coords[0]] & ~dir[2]]
    coords = (coords[0]+dir[0], coords[1]+dir[1])

timestamp('mapped out pipe')

shape = geo.Polygon(points)

contained_count = 0
for y in range(len(locs)):
    for x in range(len(locs[y])):
        point = geo.Point(x, y)
        if shape.contains(point):
            contained_count += 1

timestamp('finished')

print('Result = ', contained_count, '\n', runtimes())