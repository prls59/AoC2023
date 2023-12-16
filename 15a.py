datafile = "../../AoC/2023/15.txt"

def hash(step):
    val = 0
    for char in step:
        val = ((val + ord(char)) * 17) % 256
    return val

hash_total = 0
with open(datafile) as input:
    data = input.read()
    steps = data[:-1].split(",")
    for step in steps:
        hash_total += hash(step)

print('Result = ', hash_total)