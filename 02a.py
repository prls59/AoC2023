datafile = "../../AoC/2023/02.txt"
limits = {'red': 12, 'green': 13, 'blue': 14}

with open(datafile) as input:
    idsum = 0
    for line in input:
        line = line[0:-1] # strip off \n
        game = line.split(": ")
        id = int(game[0][5:])
        rounds = game[1].split("; ")
        for round in rounds:
            colours = round.split(", ")
            for colour in colours:
                cubes = colour.split(" ")
                if int(cubes[0])>limits[cubes[1]]:
                    id = 0
                    break
            if id == 0:
                break
        idsum += id
    print('Result = ', idsum)