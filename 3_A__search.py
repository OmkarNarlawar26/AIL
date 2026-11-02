start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def h(s):
    return sum(s[i] != goal[i] and s[i] != 0 for i in range(9))

open_list = [(h(start), 0, start, [start])]
visited = set()
costs = {start: 0}

while open_list:
    open_list.sort()

    f, g, s, path = open_list.pop(0)

    if s == goal:   
        print("Total Moves =", g)

        for p in path:
            print("\n", p[:3], "\n", p[3:6], "\n", p[6:])
            
        print("\nGoal Reached!")
        break

    if s in visited:
        continue

    visited.add(s)
    z = s.index(0)

    for d in [-3, 3, -1, 1]:
        n = z + d

        if n < 0 or n > 8 or (d == -1 and z % 3 == 0) or (d == 1 and z % 3 == 2):
            continue

        t = list(s)
        t[z], t[n] = t[n], t[z]
        t = tuple(t)

        if t not in visited and g + 1 < costs.get(t, float('inf')):
            costs[t] = g + 1
            open_list.append((g + 1 + h(t), g + 1, t, path + [t]))

else:
    print("No solution found")