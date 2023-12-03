import re
datafile = "../../AoC/2023/03.txt"

def getratio(rows, match_row, match_col):
    adjacent_numbers = []
    if match_row > 0:
        for num_match in re.finditer(r'\d+', rows[match_row-1]):
            if num_match.start() >= match_col - (num_match.end() - num_match.start()) and num_match.start() <= match_col + 1:
                adjacent_numbers.append(int(num_match.group(0)))
    for num_match in re.finditer(r'\d+', rows[match_row]):
        if num_match.start() == match_col + 1 or num_match.end() == match_col:
            adjacent_numbers.append(int(num_match.group(0)))
    if match_row < len(rows) - 1:
        for num_match in re.finditer(r'\d+', rows[match_row+1]):
            if num_match.start() >= match_col - (num_match.end() - num_match.start()) and num_match.start() <= match_col + 1:
                adjacent_numbers.append(int(num_match.group(0)))
    if len(adjacent_numbers) == 2:
        ratio = adjacent_numbers[0] * adjacent_numbers[1]
    else:
        ratio = 0
    return ratio

with open(datafile) as input:
    ratiosum = 0
    data = input.read() 
    rows = data.split("\n") 
    for row_num in range(len(rows)):
        for asterisk_match in re.finditer(r'\*', rows[row_num]):
            ratiosum += getratio(rows, row_num, asterisk_match.start())
    print('Result = ', ratiosum)