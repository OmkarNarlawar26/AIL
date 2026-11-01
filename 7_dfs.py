#  Use DFS for problem solving. Examples can be water jug problem , Missionaries and Cannibals,maze solving, blocks world etc. 

# MAZE SOLVING

grid = [
    ['S', '.', '#'],
    ['.', '.', '#'],
    ['#', '.', 'G']
]

stack = [((0, 0), [(0, 0)])]
visited = set()

while stack:
    (x, y), path = stack.pop()

    if (x, y) in visited:
        continue

    visited.add((x, y))

    if grid[x][y] == 'G':
        print("Path:", path)
        break

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy

        if (0 <= nx < 3 and 0 <= ny < 3 and
            grid[nx][ny] != '#' and (nx, ny) not in visited):

            stack.append(((nx, ny), path + [(nx, ny)]))

else:
    print("No path found!")



# WATER JUG

def dfs(a,b,visited):
    if (a,b) in visited:
        return False
    visited.add((a,b))
    print(a,b)

    if a == 2 or b == 2:
        return True

    states = [(4,b),(a,3),(0,b),(a,0),
              (a-min(a,3 - b),b + min(a,3 - b)),
              (a + min(b , 4 - a),b - min(b,4-a))]

    for x, y in states:
        if dfs(x,y,visited):
            return True
    return False

dfs(0,0,set())