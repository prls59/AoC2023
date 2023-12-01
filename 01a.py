numerals = ""

def getnumbers(string):
    out = ""
    for c in string:
        if c.isnumeric():
            out += c
    return out

try:
    input = open("01.txt")
    sum = 0
    for line in input:
        numerals = getnumbers(line)
        sum += 10*int(numerals[:1]) + int(numerals[-1:])

    print('Sum = ', sum)

finally:
    input.close()