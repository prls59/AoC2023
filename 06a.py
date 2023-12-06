import math, re

datafile = "../../AoC/2023/06testa.txt"

def getnumbers(string):
    out = []
    for number_match in re.finditer(r'\d+', string):
        out.append(int(number_match.group(0)))
    return out

def quadratic_roots(a, b, c):
    roots = []
    disc = b*b - 4*a*c
    sqrt_disc = math.sqrt(abs(disc))
    if disc >= 0:
        roots = [(-b - sqrt_disc) / (2*a), (-b + sqrt_disc) / (2*a)]
    else:
        roots = [0,0] # complex roots
    return roots

with open(datafile) as input:
    partsum = 0
    data = input.read() 
    rows = data.split("\n")
    times = getnumbers(rows[0])
    dists = getnumbers(rows[1])

product = 1
for n in range(len(times)):
    roots = quadratic_roots(1, -times[n], dists[n])
    if math.ceil(roots[0]) == roots[0]:
        roots[0] += 1
    if math.floor(roots[1]) == roots[1]:
        roots[1] -= 1
    product *= math.floor(roots[1]) - math.ceil(roots[0]) + 1

print('Result = ', product)