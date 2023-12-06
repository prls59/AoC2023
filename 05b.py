import time, bisect

datafile = "../../AoC/2023/05.txt"

SOURCE_FROM = 0
SOURCE_TO = 1
OFFSET = 2

seeds = []
s2s = []
s2f = []
f2w = []
w2l = []
l2t = []
t2h = []
h2l = []

def readmap(almanac):
# return sorted list of source range start, end, & offset to destination
    maplist = []
    for entry in almanac:
        mapping = [int(x) for x in entry[:-1].split(' ')]
        maplist.append([mapping[1],mapping[1] + mapping[2] - 1,mapping[0]-mapping[1]])
    maplist.sort()
    return maplist

def lookup(maplist, source):
# look up entry in sorted map list and return destination
    destination = source
    loc = bisect.bisect(maplist, source, key=lambda x: x[0])
    if loc in range(0,len(maplist) + 1):
        mapping = maplist[loc - 1]
        if source >= mapping[SOURCE_FROM] and source <= mapping[SOURCE_TO]:
            destination = source + mapping[OFFSET]
    return destination

with open(datafile) as input:
    line = input.readline()
    while line != '':
        prefix = line[:5]
        if prefix == '\n':
            line = input.readline()
        elif prefix == 'seeds':
            seeds = [int(x) for x in line[7:-1].split(' ')]
            line = input.readline()
        else:
            # get almanac entries
            almanac = []
            line = input.readline()
            while len(line) > 4:
                almanac.append(line)
                line = input.readline()
            # create mappings
            if prefix == 'seed-':
                s2s = readmap(almanac)
            elif prefix == 'soil-':
                s2f = readmap(almanac)
            elif prefix == 'ferti':
                f2w = readmap(almanac)
            elif prefix == 'water':
                w2l = readmap(almanac)
            elif prefix == 'light':
                l2t = readmap(almanac)
            elif prefix == 'tempe':
                t2h = readmap(almanac)
            elif prefix == 'humid':
                h2l = readmap(almanac)

closest = -1
for n in range(0, len(seeds), 2):
    seedcount = seeds[n+1]
    for m in range(seedcount):
        loc = lookup(h2l,lookup(t2h,lookup(l2t,lookup(w2l,lookup(f2w,lookup(s2f,lookup(s2s,seeds[n]+m)))))))
        if closest == -1 or loc < closest:
            closest = loc

print('Result = ', closest)