from math import gcd
from functools import reduce

datafile = "../../AoC/2023/08.txt"
network = {}

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

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

zdists = [] # list of distances to first z node 
for x in network.keys():
    if x[-1:] == 'A':
        loc = x
        steps = 0
        while loc[-1:] != 'Z':
            loc = network[loc][turns[steps%turn_count]]
            steps += 1
        zdists.append(steps)

print('Result = ', lcm(zdists))