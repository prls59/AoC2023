import math, re

datafile = "../../AoC/2023/06.txt"

def getnumbers(string):
    out = ""
    for number_match in re.finditer(r'\d+', string):
        out += number_match.group(0)
    return [int(out)]

def quadratic_roots(a, b, c):
    disc = math.sqrt(abs(b*b - 4*a*c))
    roots = [(-b - disc) / (2*a), (-b + disc) / (2*a)]
    return roots

with open(datafile) as input:
    partsum = 0
    data = input.read() 
    rows = data.split("\n")
    times = getnumbers(rows[0])
    dists = getnumbers(rows[1])

product = 1
for n in range(len(times)):
    roots = quadratic_roots(1, -times[n], dists[n] + 1)
    product *= math.floor(roots[1]) - math.ceil(roots[0]) + 1

print('Result = ', product)