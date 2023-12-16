datafile = "../../AoC/2023/16.txt"

# contraption grid
EMPTY = 0b00000001
MIRROR_R = 0b00000010
MIRROR_L = 0b00000100
SPLITTER_V = 0b00001000
SPLITTER_H = 0b00010000
BEAM_V = 0b00100000
BEAM_H = 0b01000000

# beam directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

DELTA = ((0,-1),(0,1),(-1,0),(1,0))
BREADCRUMBS = (BEAM_V, BEAM_V, BEAM_H, BEAM_H)
REFLECT_R = (RIGHT, LEFT, DOWN, UP)
REFLECT_L = (LEFT, RIGHT, UP, DOWN)
SPLIT_V = (EMPTY, EMPTY, ~EMPTY, ~EMPTY)
SPLIT_H = (~EMPTY, ~EMPTY, EMPTY, EMPTY)

# coords indices
X = 0
Y = 1

reset = []
contraption = []
beams = []

def set_flag(char):
    if char == '.':
        flag = EMPTY
    elif char == '/':
        flag = MIRROR_R
    elif char == '\\':
        flag = MIRROR_L
    elif char == '|':
        flag = SPLITTER_V
    else:
        flag = SPLITTER_H
    return flag


def shine(vector):
    coords = (vector[0][0],vector[0][1])
    direction = vector[1]
    if coords[X] < 0 or coords[X] >= num_cols or coords[Y] < 0 or coords[Y] >= num_rows:
        return
    cell = contraption[coords[Y]][coords[X]]
    if cell & BREADCRUMBS[direction] == BREADCRUMBS[direction] and cell & (MIRROR_L | MIRROR_R) == 0:
        return
    else:
        contraption[coords[Y]][coords[X]] = cell | BREADCRUMBS[direction]
        if cell & EMPTY == EMPTY:
            beams.append(((coords[X]+DELTA[direction][X],coords[Y]+DELTA[direction][Y]),direction))
        elif cell & MIRROR_R == MIRROR_R:
            new_dir = REFLECT_R[direction]
            beams.append(((coords[X]+DELTA[new_dir][X],coords[Y]+DELTA[new_dir][Y]),new_dir))
        elif cell & MIRROR_L == MIRROR_L:
            new_dir = REFLECT_L[direction]
            beams.append(((coords[X]+DELTA[new_dir][X],coords[Y]+DELTA[new_dir][Y]),new_dir))
        elif cell & SPLITTER_V == SPLITTER_V:
            if SPLIT_V[direction] == EMPTY:
                beams.append(((coords[X],coords[Y]+DELTA[direction][Y]),direction))
            else:
                beams.append(((coords[X],coords[Y]-1),UP))
                beams.append(((coords[X],coords[Y]+1),DOWN))
        elif cell & SPLITTER_H == SPLITTER_H:
            if SPLIT_H[direction] == EMPTY:
                beams.append(((coords[X]+DELTA[direction][X],coords[Y]),direction))
            else:
                beams.append(((coords[X]-1,coords[Y]),LEFT))
                beams.append(((coords[X]+1,coords[Y]),RIGHT))
    return

def check(setup):
    global beams, contraption
    contraption = [list(x) for x in reset]
    beams = [setup]
    step = 0
    while step < len(beams):
        shine(beams[step])
        step += 1

    energised = 0
    for row in contraption:
        for cell in row:
            if cell & (BEAM_V | BEAM_H):
                energised += 1
    return energised

with open(datafile) as input:
    data = input.read() 
    rows = data[:-1].split("\n")
    for row in rows:
        reset.append([set_flag(x) for x in row])

num_rows = len(reset)
num_cols = len(reset[0])
max_energised = 0

for y in range(num_rows):
    a = check(((0,y),RIGHT))
    b = check(((num_cols - 1,y),LEFT))
    max_energised = max(a, b, max_energised)

for x in range(num_cols):
    a = check(((x,0),DOWN))
    b = check(((x,num_rows - 1),UP))
    max_energised = max(a, b, max_energised)

print('Result = ', max_energised)