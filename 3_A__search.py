from heapq import heappush,heappop

goal = (1,2,3,4,5,6,7,8,9,0)

def h(s):
    return sum(s[i] != 0 and s[i] != goal[i] for i in range(9))

def solve(start):
    pq = [(h(start),0,start,[])]
    visited = set()

    while pq:
        f,g,s,path = heappop(pq)
        if s == goal:
            return path + [s]
        if s in visited:
            continue
        visited.add(s)

        z = s.index(0)
        for n in ([z-3] if z>=3 else []) + ([z+3] if z<6 else []) + ([z-1] if z%3 else []) + ([z+1] if z%3<2 else []):
            t = list(s)
            t[z],t(n) = t[n], t[z]
            t = tuple(t)
            if t not in visited:
                heappush(pq,(g+1+h(t) , g + 1,t,path,+[s]))
    return None

start = (1,2,3,4,0,5,6,7,8)
result = solve(start)

if result:
    for s in result:
        print(s[:3],s[3:6],s[6:])
        print()
else:
    print("No solution")