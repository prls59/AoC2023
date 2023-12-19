import copy

datafile = "../../AoC/2023/19.txt"

cat_index = {'x':0,'m':1,'a':2,'s':3}
MIN_RATING = 1
MAX_RATING = 4000
MIN = 0
MAX = 1

def show(workflows, title):
    print(title, len(workflows),' entries')
'''
    for (key, value) in workflows.items():
        print(key,'{',value,'}')
'''

def replace_wf(wf, action):
    workflows.pop(wf, None)
    for key in workflows.keys():
        for rule in workflows[key]:
            if rule[-1] == wf:
                rule[-1] = action
    return

#
# Load workflows
#
workflows = {}
parts = []
with open(datafile) as input:
    for line in input:
        if line == '\n':
            break
        else:
            rule_start = line.find('{')
            name = line[:rule_start]
            rules = []
            rule_strs = line[rule_start + 1:-2].split(',')
            for rule_str in rule_strs:
                colon = rule_str.find(':')
                if colon >= 0:
                    rules.append([rule_str[0],rule_str[1],int(rule_str[2:colon]),rule_str[colon+1:]])
                else:
                    rules.append([rule_str[colon+1:]])
            workflows[name] = rules

show(workflows, 'Original:  ')


#
# Remove redundant workflows
#
simplify = True
while simplify:
    for wf in workflows.keys():
        action = ''
        simplify = True
        for rule in workflows[wf]:
            if action == '':
                action = rule[-1]
            else:
                if rule[-1] != action:
                    simplify = False
                    break
        if simplify:
            replace_wf(wf, action)
            break

show(workflows, 'Simplified:')

#
# Follow workflows
#
queue = [['in',[[MIN_RATING, MAX_RATING] for x in range(4)]]]
paths = []
while len(queue) > 0:
    (name, rating_limits) = queue.pop(0)
    for rule in workflows[name]:
        if len(rule) == 1:
            if rule[0] == 'A':
                paths.append(rating_limits)
            elif rule[0] != 'R':
                queue.append([rule[0], rating_limits])
            break
        else:
            cat = rule[0]
            com = rule[1]
            val = rule[2]
            new = rule[3]
            if com == '<':
                if rating_limits[cat_index[cat]][MIN] < val and new != 'R':
                    copy_list = copy.deepcopy(rating_limits)
                    if copy_list[cat_index[cat]][MAX] >= val:
                        copy_list[cat_index[cat]][MAX] = val - 1
                        if new == 'A':
                            paths.append(copy_list)
                        else:
                            queue.append([new, copy_list])
                if rating_limits[cat_index[cat]][MAX] < val:
                    break
                else:
                    if rating_limits[cat_index[cat]][MIN] < val:
                        rating_limits[cat_index[cat]][MIN] = val
            elif com == '>':
                if rating_limits[cat_index[cat]][MAX] > val and new != 'R':
                    copy_list = copy.deepcopy(rating_limits)
                    if copy_list[cat_index[cat]][MIN] <= val:
                        copy_list[cat_index[cat]][MIN] = val + 1
                        if new == 'A':
                            paths.append(copy_list)
                        else:
                            queue.append([new, copy_list])
                if rating_limits[cat_index[cat]][MIN] > val:
                    break
                else:
                    if rating_limits[cat_index[cat]][MAX] > val:
                        rating_limits[cat_index[cat]][MAX] = val

combo_tot = 0
for path in paths:
    combos = 1
    for cat in cat_index.values():
        combos *= path[cat][MAX] - path[cat][MIN] + 1
    combo_tot += combos

print('Result = ', combo_tot)