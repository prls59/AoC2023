import re
datafile = "../../AoC/2023/04.txt"
MATCHES = 0
COPIES = 1
cards = []
card_num = 0

with open(datafile) as input:
    for line in input:
        line = line[0:-1] # strip off \n
        parts = line[line.find(':')+1:].split(' | ')
        winners = []
        scratch_nums = []
        for number_match in re.finditer(r'\d+', parts[0]):
            winners.append(int(number_match.group(0)))
        for number_match in re.finditer(r'\d+', parts[1]):
            scratch_nums.append(int(number_match.group(0)))

        matching_nums = 0
        for scratch_num in scratch_nums:
            if scratch_num in winners:
                matching_nums += 1
        cards.append([matching_nums, 1])

# create & count the copies    
tot_cards = 0
for n in range(len(cards)):
    tot_cards += cards[n][COPIES]
    if cards[n][MATCHES] > 0:
        for m in range(1,cards[n][MATCHES]+1):
            cards[n+m][COPIES] += cards[n][COPIES]

print('Result = ', tot_cards)