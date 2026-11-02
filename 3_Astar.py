goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

def heuristic(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def display(state):
    print(state[:3])
    print(state[3:6])
    print(state[6:])
    print()

def astar(start):
    open_list = [(start, 0)]
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: x[1] + heuristic(x[0]))
        state, cost = open_list.pop(0)

        if tuple(state) in visited:
            continue

        display(state)

        if state == goal:
            print("Goal Reached!")
            return

        visited.add(tuple(state))

        zero = state.index(0)
        moves = []

        if zero > 2:
            moves.append(zero - 3)
        if zero < 6:
            moves.append(zero + 3)
        if zero % 3 != 0:
            moves.append(zero - 1)
        if zero % 3 != 2:
            moves.append(zero + 1)

        for pos in moves:
            new_state = state[:]
            new_state[zero], new_state[pos] = new_state[pos], new_state[zero]

            if tuple(new_state) not in visited:
                open_list.append((new_state, cost + 1))

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

print("Initial State:")
display(start)

astar(start)