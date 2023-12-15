datafile = "../../AoC/2023/14.txt"

UNKNOWN = -1
tot_weight = 0
platform = []

with open(datafile) as input:
    data = input.read() 
    rows = data[:-1].split("\n")
    for row in rows:
        platform.append([x for x in row])

row_count = len(platform)
col_count = len(platform[0])

for col_num in range(col_count):
    load = row_count
    for row_num in range(row_count):
        sym = platform[row_num][col_num]
        if sym == '#':
            load = UNKNOWN
        else:
            if load == UNKNOWN:
                load = row_count - row_num
            if sym == 'O':
                tot_weight += load
                load -= 1

print('Result = ', tot_weight)