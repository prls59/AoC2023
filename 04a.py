import re
datafile = "../../AoC/2023/04.txt"

with open(datafile) as input:
    tot_points = 0
    for line in input:
        line = line[0:-1] # strip off \n
        parts = line[line.find(':')+1:].split(' | ')
        winners = []
        card_nums = []
        for number_match in re.finditer(r'\d+', parts[0]):
            winners.append(int(number_match.group(0)))
        for number_match in re.finditer(r'\d+', parts[1]):
            card_nums.append(int(number_match.group(0)))

        matches = 0
        for card_num in card_nums:
            if card_num in winners:
                matches += 1
        if matches > 0:
            tot_points += 2**(matches-1)

    print('Result = ', tot_points)