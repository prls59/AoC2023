# Adapted from u/Diderikdm's solution at https://www.reddit.com/r/adventofcode/comments/18ge41g/2023_day_12_solutions/

from functools import cache

datafile = "../../AoC/2023/12.txt"

@cache
def count_arrangments(remaining_report_line, remaining_spring_list, result=0):
    if len(remaining_spring_list) == 0:
        # no springs left in spring list: okay provided no springs remain in remaining conditions report
        return '#' not in remaining_report_line
    contiguous_springs_expected_here, remaining_spring_list = remaining_spring_list[0], remaining_spring_list[1:]
    for i in range(len(remaining_report_line) - sum(remaining_spring_list) - len(remaining_spring_list) - contiguous_springs_expected_here + 1):
        if "#" in remaining_report_line[:i]:
            break
        next_pos = i + contiguous_springs_expected_here
        if next_pos <= len(remaining_report_line) and '.' not in remaining_report_line[i : next_pos] and remaining_report_line[next_pos : next_pos + 1] != "#":
            result += count_arrangments(remaining_report_line[next_pos + 1:], remaining_spring_list)
    return result


with open(datafile) as input:
    data = [x.split() for x in input.read().splitlines()]
    arrangements = 0
    for report, spring_list in data:
        # unfold...
        report = "?".join([report] * 5)
        spring_list = tuple(map(int, spring_list.split(","))) * 5
        arrangements += count_arrangments(report, spring_list)
    print('Result = ', arrangements)