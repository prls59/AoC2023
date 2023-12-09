import re
datafile = "../../AoC/2023/09.txt"

def next_value(seq):
    if seq[-2] == seq[-1]:
        return seq[-1]
    else:
        subseq = []
        for n in range(1,len(seq)):
            subseq.append(seq[n]-seq[n-1])
        return seq[-1] + next_value(subseq)

with open(datafile) as input:
    next_sum = 0
    for line in input:
        seq = [int(x) for x in line[:-1].split()]
        next_sum += next_value(seq)

print('Result = ', next_sum)