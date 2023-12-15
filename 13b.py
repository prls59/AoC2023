datafile = "../../AoC/2023/13.txt"
outfile = "../../AoC/2023/13out.txt"

HORIZ = 0
VERT = 1
SHOW = False

def smudgy_match(list1, list2):
    diffs = 0
    for n in range(min(len(list1),len(list2))):
        diffs += 0 if list1[n] == list2[n] else 1
        if diffs > 1:
            break
    return diffs

def find_mirror(pattern):
    loc = 0
    for n in range(0, len(pattern) - 1):
        mirror_found = True
        smudges = 0
        for m in range(min(n + 1,len(pattern) - n - 1)):
            smudges += smudgy_match(pattern[n-m], pattern[n+m+1])
            if smudges > 1:
                mirror_found = False
                break
        if mirror_found and smudges == 1:
            loc = n + 1
            break
    return loc

def process_pattern(pattern):
    return_val = 0
    if SHOW:
        copy = pattern
    # look for row-based symmetry
    mirror_loc = find_mirror(pattern)
    if mirror_loc > 0:
        return_val += 100 * mirror_loc
        if SHOW:
            print_pattern(copy, mirror_loc, HORIZ)
    else:
        # look for column-based symmetry
        pattern = [list(i) for i in zip(*pattern)]
        mirror_loc = find_mirror(pattern)
        return_val += mirror_loc
        if SHOW:
            print_pattern(copy, mirror_loc, VERT)
    return return_val

def print_pattern(pattern, mirror_loc, orientation):
    if orientation == VERT:
        output.write(' ' * mirror_loc + '><\n')
        for row in pattern:
            output.write(' ')
            for char in row:
                output.write(char)
            output.write('\n')
        output.write(' ' * mirror_loc + '><\n')
    else:
        for n in range(len(pattern)):
            if n == mirror_loc-1:
                output.write('v')
            elif n == mirror_loc:
                output.write('^')
            else:
                output.write(' ')
            for char in pattern[n]:
                output.write(char)
            if n == mirror_loc-1:
                output.write('v')
            elif n == mirror_loc:
                output.write('^')
            output.write('\n')
    output.write('\n')
    return

pattern = []
mirror_sum = 0
if SHOW:
    output = open(outfile, 'wt')
with open(datafile) as input:
    for line in input:
        row = line[:-1]
        if row == "":
            mirror_sum += process_pattern(pattern)
            # reset for next pattern
            pattern = []
        else:
            pattern.append([x for x in row])
mirror_sum += process_pattern(pattern) # final pattern
if SHOW:
    output.close()
print('Result: ', mirror_sum)