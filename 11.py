import re
datafile = "../../AoC/2023/11.txt"

speed = 1000000

galaxies = []
with open(datafile) as input:
    y = 0
    for line in input:
        found_galaxies = False
        galaxy_matches = re.finditer('#', line[:-1])
        for galaxy_match in galaxy_matches:
            found_galaxies = True
            galaxies.append([galaxy_match.start(0),y])
        y += 1 if found_galaxies else speed

galaxies.sort()
prev_x = 0
expansion = 0
for galaxy in galaxies:
    gap = galaxy[0] - prev_x
    prev_x = galaxy[0]
    expansion += (speed - 1) * max(gap - 1, 0)
    galaxy[0] += expansion

num_galaxies = len(galaxies)
path_sum = 0
for n in range(num_galaxies):
    galaxy = galaxies[n]
    for m in range(n+1, num_galaxies):
        path_sum += abs(galaxies[m][0] - galaxy[0]) + abs(galaxies[m][1] - galaxy[1])

print('Result = ', path_sum)