datafile = "../../AoC/2023/01.txt"
numerals = ""
numwords = ["one","two","three","four","five","six","seven","eight","nine"]

def getnumbers(line):
    out = ""
    for n in range(len(line)):
        c = line[n:n+1]
        if c.isnumeric():
            out += c
        else:
            for x in range(9):
                if line[n:n+len(numwords[x])] == numwords[x]:
                    out += str(x+1)
    return out

try:
    input = open(datafile)
    sum = 0
    for line in input:
        numerals = getnumbers(line)
        sum += 10*int(numerals[:1]) + int(numerals[-1:])

    print('Sum = ', sum)

finally:
    input.close()