import re
datafile = "../../AoC/2023/03.txt"

def partnumber(rows, match_row, match_start, match_end):
    is_part = False
    if match_start > 0 and rows[match_row][match_start-1:match_start] != ".":
        is_part = True
    elif match_end < len(rows[match_row]) and rows[match_row][match_end:match_end+1] != ".":
        is_part = True
    else:
        if match_row > 0:
            for x in range(max(0,match_start - 1),min(len(rows[match_row - 1]),match_end + 1)):
                c = rows[match_row - 1][x:x+1]
                if c != "." and not c.isnumeric():
                    is_part = True
                    break
        if not is_part and match_row < len(rows) - 1:
            for x in range(max(0,match_start - 1),min(len(rows[match_row + 1]),match_end + 1)):
                c = rows[match_row + 1][x:x+1]
                if c != "." and not(c.isnumeric()):
                    is_part = True
                    break
    return is_part

with open(datafile) as input:
    partsum = 0
    data = input.read() 
    rows = data.split("\n") 
    for row_num in range(len(rows)):
        for number_match in re.finditer(r'\d+', rows[row_num]):
            if partnumber(rows, row_num, number_match.start(), number_match.end()):
                partsum += int(number_match.group(0))
    print('Result = ', partsum)