import queue

datafile = "../../AoC/2023/17.txt"

def available_locs(curr_loc_mom, x_lim, y_lim, straight_min, straight_max):
    steps = []
    (curr_loc, vector, dist) = curr_loc_mom

    if dist < straight_max:
        if vector == (0, 0):
            steps.append(((curr_loc[0] + 1, curr_loc[1]), (1, 0), 1))
            steps.append(((curr_loc[0], curr_loc[1] + 1), (0, 1), 1))
        else:
            new_loc = (curr_loc[0] + vector[0], curr_loc[1] + vector[1])
            if in_bounds(new_loc, x_lim, y_lim):
                steps.append((new_loc, vector, dist + 1))
    if dist >= straight_min:
        new_vector = (vector[1], vector[0])
        new_loc = (curr_loc[0] + new_vector[0], curr_loc[1] + new_vector[1])
        if in_bounds(new_loc, x_lim, y_lim):
            steps.append((new_loc, new_vector, 1))
        new_vector = (0 - vector[1], 0 - vector[0])
        new_loc = (curr_loc[0] + new_vector[0], curr_loc[1] + new_vector[1])
        if in_bounds(new_loc, x_lim, y_lim):
            steps.append((new_loc, new_vector, 1))
    return steps

def in_bounds(loc, x_lim, y_lim):
    return 0 <= loc[0] < x_lim and 0 <= loc[1] < y_lim

def dijkstra(city_map, start_loc_mom, goal_loc):
    frontier = queue.PriorityQueue()
    frontier.put((0, start_loc_mom))
    from_dict = {}
    cost_dict = {}
    from_dict[start_loc_mom] = None
    cost_dict[start_loc_mom] = 0
    
    while not frontier.empty():
        (_, curr_loc_mom) = frontier.get()
        
        (curr_loc, _, _) = curr_loc_mom
        if curr_loc == goal_loc:
            break

        next_loc_moms = available_locs(curr_loc_mom, x_lim, y_lim, straight_min=4, straight_max=10)
        for next_loc_mom in next_loc_moms:
            (next_loc, vector, dist) = next_loc_mom
            new_cost = cost_dict[curr_loc_mom] + city_map[next_loc[1]][next_loc[0]]
            if next_loc_mom not in cost_dict or new_cost < cost_dict[next_loc_mom]:
                cost_dict[next_loc_mom] = new_cost
                priority = new_cost
                frontier.put((priority, next_loc_mom))
                from_dict[next_loc_mom] = curr_loc_mom
    
    return from_dict, cost_dict

city_map = []
with open(datafile) as input:
    data = input.read()
rows = data[:-1].split("\n")
for row in rows:
    city_map.append([int(x) for x in row])
x_lim = len(city_map[0])
y_lim = len(city_map)

start_loc_mom = ((0, 0), (0, 0), 0)
goal_loc = (x_lim - 1, y_lim - 1)

from_dict, cost_dict = dijkstra(city_map, start_loc_mom, goal_loc)

shortest = -1
end = ()
for loc_mom in cost_dict.keys():
    (loc, _, _) = loc_mom
    if loc == goal_loc:
        if shortest == -1 or cost_dict[loc_mom] < shortest:
            shortest = cost_dict[loc_mom]
            end = loc_mom

print('Result = ', shortest)
'''
loc_mom = end
while loc_mom != start_loc_mom:
    (loc, _, _) = loc_mom
    city_map[loc[1]][loc[0]] = '#'
    loc_mom = from_dict[loc_mom]

for row in city_map:
    for col in row:
        print(col, end = '')
    print('')
'''