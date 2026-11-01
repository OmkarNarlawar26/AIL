#  Use BFS to solve a planning problem. Examples can be 8 puzzle problem, Robot path planning,Blocks world etc. 

from collections import deque

grid = [
    ['S','.','#'],
    ['.','.','#'],
    ['#','.','G']
]

q = deque([((0,0),[(0,0)])])
visited = {(0,0)}

while q:
    (x,y), path = q.popleft()

    if grid[x][y] == 'G':
        print("Path:", path)
        break

    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx,ny = x + dx, y + dy

        if (0 <= nx < 3 and 0 <= ny < 3 and
            grid[nx][ny] != '#' and (nx,ny) not in visited):

            visited.add((nx,ny))
            q.append(((nx,ny),path+[(nx,ny)]))

else:
    print("No path found!")