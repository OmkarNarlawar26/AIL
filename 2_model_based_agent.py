#  Implement a model-based intelligent agent capable of navigating a grid environment with obstacles using internal state representation. 

grid = [
    ['S','.','#'],
    ['#','.','#'],
    ['.','.','G']
]

pos = (0,0)
visited = set()

print("Starting Position :", pos)

while(pos != (2,2)):
    visited.add(pos)
    x, y = pos

    if y + 1 < 3 and grid[x][y + 1] != '#' and (x,y + 1) not in visited:
        pos = (x,y + 1)
    elif x + 1 < 3 and grid[x + 1][y] != '#' and (x + 1,y) not in visited:
        pos = (x + 1,y)
    elif y - 1 >= 0 and grid[x][y - 1] != '#' and (x,y - 1) not in visited:
        pos = (x, y - 1)
    elif x - 1 >= 0 and grid[x - 1][y] != '#' and (x - 1,y) not in visited:
        pos = (x - 1,y)
    else:
        print("No path found!")
        break

    print("Current Position : ",pos)

if pos == (2,2):
    print("Goal Reached!")