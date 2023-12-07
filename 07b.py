datafile = "../../AoC/2023/07.txt"
hands = []

def hand_type(cards_input):
    # returns a hand type value that is sortable for camel poker:
    # 9 = five of a kind, 7 = four of a kind, 6 = full house, 5 = three of a kind,
    # 4 = two pairs, 3 = one pair, 1 = high card
    # Jokers are factored in at the end
    cards = sorted(cards_input)
    prev = ''
    group_count = 0
    group_length = 0
    longest_group = 1
    joker_count = 0
    for card in cards:
        if card == 'J':
            joker_count += 1
        elif card == prev:
            group_length += 1
            if group_length > longest_group:
                longest_group = group_length
        else:
            group_count += 1
            group_length = 1
        prev = card
    return str(longest_group + min(joker_count, 4) + 5 - max(group_count, 1))

def sortable_hand(cards_input):
    # returns a string representing a hand of cards that is sortable for camel poker:
    # Court cards & the joker are translated from A -> X, K -> W, Q -> V, J -> 1
    cards = cards_input
    for trans in [['J','1'],['Q','V'],['K','W'],['A','X']]:
        cards = cards.replace(trans[0], trans[1])
    return cards

def camelsort(hand):
# return key based on hand type and translated card denominations
    return hand_type(hand[0]) + sortable_hand(hand[0])

with open(datafile) as input:
    for line in input:
        hands.append(line[0:-1].split(' '))

hands.sort(key=camelsort)

bidsum = 0
for n in range(len(hands)):
    bidsum += (n + 1) * int(hands[n][1])

print('Result = ', bidsum)