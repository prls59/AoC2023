datafile = "../../AoC/2023/10.txt"

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

for dir in directions.values():
    coords = (start_coords[0]+dir[0], start_coords[1]+dir[1])
    if coords[0] >= 0 and coords[0] < len(locs[0]) and coords[1] >= 0 and coords[1] < len(locs):
        if locs[coords[1]][coords[0]] & dir[2] != 0:
            break

loop_length = 1
while locs[coords[1]][coords[0]] != START:
    dir = directions[locs[coords[1]][coords[0]] & ~dir[2]]
    coords = (coords[0]+dir[0], coords[1]+dir[1])
    loop_length += 1
        
print('Result = ', (loop_length) // 2)