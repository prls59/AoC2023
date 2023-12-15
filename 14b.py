datafile = "../../AoC/2023/14.txt"
outfile = "../../AoC/2023/14out.txt"

DEBUG = False

NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3

EMPTY = '.'
CUBE = '#'
ROUND = 'O'

UNKNOWN = -1
platform = []
history = []

CYCLES = 1000000000

def tip(direction):
    if direction == NORTH:
        for col_num in range(col_count):
            dest = 0
            for row_num in range(row_count):
                sym = platform[row_num][col_num]
                if sym == CUBE:
                    dest = UNKNOWN
                else:
                    if dest == UNKNOWN:
                        dest = row_num
                    if sym == ROUND:
                        if dest != row_num:
                            platform[dest][col_num] = ROUND
                            platform[row_num][col_num] = EMPTY
                        dest += 1
    elif direction == WEST:
        for row_num in range(row_count):
            dest = 0
            for col_num in range(col_count):
                sym = platform[row_num][col_num]
                if sym == CUBE:
                    dest = UNKNOWN
                else:
                    if dest == UNKNOWN:
                        dest = col_num
                    if sym == ROUND:
                        if dest != col_num:
                            platform[row_num][dest] = ROUND
                            platform[row_num][col_num] = EMPTY
                        dest += 1
    elif direction == SOUTH:
        for col_num in range(col_count):
            dest = row_count - 1
            for row_num in range(row_count - 1, -1, -1):
                sym = platform[row_num][col_num]
                if sym == CUBE:
                    dest = UNKNOWN
                else:
                    if dest == UNKNOWN:
                        dest = row_num
                    if sym == ROUND:
                        if dest != row_num:
                            platform[dest][col_num] = ROUND
                            platform[row_num][col_num] = EMPTY
                        dest -= 1
    elif direction == EAST:
        for row_num in range(row_count):
            dest = col_count - 1
            for col_num in range(col_count - 1, -1, -1):
                sym = platform[row_num][col_num]
                if sym == CUBE:
                    dest = UNKNOWN
                else:
                    if dest == UNKNOWN:
                        dest = col_num
                    if sym == ROUND:
                        if dest != col_num:
                            platform[row_num][dest] = ROUND
                            platform[row_num][col_num] = EMPTY
                        dest -= 1
    return

def spin():
    tip(NORTH)
    tip(WEST)
    tip(SOUTH)
    tip(EAST)
    return

def north_load():
    load = 0
    for row_num in range(row_count):
        load += sum((row_count - row_num) if x == ROUND else 0 for x in platform[row_num])
    return load

def show(label, plat):
    output.write(label + ':\n')
    for row in plat:
        output.write(''.join(row) + '\n')
    output.write('\n')
    return

def record(plat):
    platstring = ""
    for row in plat:
        platstring += ''.join(row)
    history.append(platstring)
    return

def already_seen(plat):
    loc = UNKNOWN
    platstring = ""
    for row in plat:
        platstring += ''.join(row)
    if platstring in history:
        loc = history.index(platstring)
    return loc

with open(datafile) as input:
    data = input.read() 
    rows = data[:-1].split("\n")
    for row in rows:
        platform.append([x for x in row])

row_count = len(platform)
col_count = len(platform[0])
record(platform)

if DEBUG:
    output = open(outfile, 'wt')
    show('start',platform)

for n in range(CYCLES):
    spin()
    if DEBUG:
        show('n = ' + str(n),platform)
    prev = already_seen(platform)
    if prev == UNKNOWN:
        record(platform)
    else:
        if DEBUG:
            print(CYCLES, ' - ', prev, ' = ', CYCLES - prev, ' and ', n + 1, ' - ', prev, ' = ', n - prev)
        if (CYCLES - prev) % (n + 1 - prev) == 0:
            break

if DEBUG:
    output.close()
print('Result = ', north_load())