datafile = "../../AoC/2023/08.txt"
network = {}

with open(datafile) as input:

    turn_string = input.readline()[:-1]
    turns = [0 if x == 'L' else 1 for x in turn_string]
    turn_count = len(turns)

    line = input.readline()
    line = input.readline()
    while line != '':
        entry = line[:-1].split(' = ')
        to_nodes = entry[1][1:-1].split(', ')
        network[entry[0]] = to_nodes
        line = input.readline()

steps = 0
loc = 'AAA'

while loc != 'ZZZ':
    loc = network[loc][turns[steps%turn_count]]
    steps += 1

print('Result = ', steps)