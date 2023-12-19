datafile = "../../AoC/2023/19.txt"

def next_value(seq):
    if seq[-2] == seq[-1]:
        return seq[-1]
    else:
        subseq = []
        for n in range(1,len(seq)):
            subseq.append(seq[n]-seq[n-1])
        return seq[-1] + next_value(subseq)

workflows = {}
parts = []
with open(datafile) as input:
    loading_workflows = True
    for line in input:
        if line == '\n':
            loading_workflows = False
            continue
        if loading_workflows:
            rule_start = line.find('{')
            name = line[:rule_start]
            rules = []
            rule_strs = line[rule_start + 1:-2].split(',')
            for rule_str in rule_strs:
                colon = rule_str.find(':')
                if colon >= 0:
                    rules.append((rule_str[0],rule_str[1],int(rule_str[2:colon]),rule_str[colon+1:]))
                else:
                    rules.append((rule_str[colon+1:],))
            workflows[name] = rules
        else:
            cat_strs = line[1:-2].split(',')
            ratings = {}
            for cat_str in cat_strs:
                ratings[cat_str[0]] = int(cat_str[2:])
            parts.append(ratings)

tot_ratings = 0
for part in parts:
    action = 'in'
    while action not in ['A','R']:
        rules = workflows[action]
        for rule in rules:
            if len(rule) == 1:
                action = rule[0]
                break
            else:
                if (rule[1] == '<' and part[rule[0]] < rule[2]) or (rule[1] == '>' and part[rule[0]] > rule[2]):
                    action = rule[3]
                    break
    if action == 'A':
        tot_ratings += part['x'] + part['m'] + part['a'] + part['s']

print('Result = ', tot_ratings)