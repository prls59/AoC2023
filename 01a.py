datafile = "../../AoC/2023/01.txt"
numerals = ""

def getnumbers(string):
    out = ""
    for c in string:
        if c.isnumeric():
            out += c
    return out

with open(datafile) as input:
    sum = 0
    for line in input:
        numerals = getnumbers(line)
        sum += 10*int(numerals[:1]) + int(numerals[-1:])

    print('Sum = ', sum)