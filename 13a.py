datafile = "../../AoC/2023/13.txt"

def find_mirror(pattern):
    loc = 0
    for n in range(0, len(pattern) - 1):
        mirror_found = True
        for m in range(min(n + 1,len(pattern) - n - 1)):
            if pattern[n-m] != pattern[n+m+1]:
                mirror_found = False
                break
        if mirror_found:
            loc = n + 1
            break
    return loc

def process_pattern(pattern):
    return_val = 0
    # look for row-based symmetry
    mirror_loc = find_mirror(pattern)
    if mirror_loc > 0:
        return_val += 100 * mirror_loc
    else:
        # look for row-based symmetry
        pattern = [list(i) for i in zip(*pattern)]
        return_val += find_mirror(pattern)
    return return_val

pattern = []
mirror_sum = 0
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
print('Result: ', mirror_sum)