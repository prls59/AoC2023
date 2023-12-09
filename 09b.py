import re
datafile = "../../AoC/2023/09.txt"

def prev_value(seq):
    if all([x == 0 for x in seq]):
        return 0
    else:
        subseq = []
        for n in range(1,len(seq)):
            subseq.append(seq[n]-seq[n-1])
        return seq[0] - prev_value(subseq)

with open(datafile) as input:
    prev_sum = 0
    for line in input:
        seq = [int(x) for x in line[:-1].split()]
        prev_sum += prev_value(seq)

print('Result = ', prev_sum)