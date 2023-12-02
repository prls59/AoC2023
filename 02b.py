from functools import reduce
datafile = "../../AoC/2023/02.txt"
index = {'red': 0, 'green': 1, 'blue': 2}

try:
    input = open(datafile)
    powersum = 0
    for line in input:
        line = line[0:-1] # strip off \n
        game = line.split(": ")
#       id = int(game[0][5:])
        minima = [0, 0, 0]
        rounds = game[1].split("; ")
        for round in rounds:
            colours = round.split(", ")
            for colour in colours:
                cubes = colour.split(" ")
                if int(cubes[0])>minima[index[cubes[1]]]:
                    minima[index[cubes[1]]] = int(cubes[0])
        powersum += reduce((lambda x, y: x * y), minima)
    print('Result = ', powersum)

finally:
    input.close()