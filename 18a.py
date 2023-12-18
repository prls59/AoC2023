import math
from shapely.geometry import Polygon 

datafile = "../../AoC/2023/18.txt"

points = []
prev = [0,0]
points.append(prev)

perim = 0

with open(datafile) as input:
    for line in input:
        dir, lstr, colour = line[:-1].split()
        length = int(lstr)
        perim += length
        if dir == 'R':
            new_point = (prev[0] + length, prev[1])
        elif dir == 'L':
            new_point = (prev[0] - length, prev[1])
        elif dir == 'U':
            new_point = (prev[0], prev[1] - length)
        else:
            new_point = (prev[0], prev[1] + length)
        points.append(list(new_point))
        prev = new_point

poly = Polygon(points)
print('Result = ', 1 + math.floor(poly.area) + perim // 2)