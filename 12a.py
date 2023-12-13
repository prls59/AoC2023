import itertools
import math
datafile = "../../AoC/2023/12.txt"

def valid(cand, row):
    result = True
    for n in range(len(cand)):
        if row[n] != '?' and cand[n] != row[n]:
            result = False
            break
    return result

with open(datafile) as input:
    arrangements = 0
    for line in input:
        arr = 0
        row = line[:-1].split()
        cgroups = [int(x) for x in row[1].split(',')]
        extra = len(row[0]) - (sum(cgroups) + len(cgroups) - 1)
        if extra == 0:
            arr += 1
        else:
            gaps = ""
            for n in range(len(cgroups)+1):
                gaps += str(n).strip()
            combos = itertools.combinations_with_replacement(gaps, extra)
            for combo in combos:
                padding = [1 for x in gaps]
                padding[0] = 0
                padding[-1] = 0
                for n in range(extra):
                    padding[int(combo[n])] += 1
                candidate = '.' * int(padding[0])
                for n in range(len(cgroups)):
                    candidate += '#' * cgroups[n]
                    candidate += '.' * padding[n+1]
                if valid(candidate, row[0]):
                    arr += 1
        arrangements += arr

print('Result: ', arrangements)