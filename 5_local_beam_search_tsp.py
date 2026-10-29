import random

dist = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]

def cost(path):
    return sum(dist[path[i]][path[i+1]] for i in range(len(path)-1)) + dist[path[-1]][path[0]]

n,k = 4,3
beam = [random.sample(range(n),n) for _ in range(k)]

for _ in range(100):
    candidates = []
    for p in beam:
        for i in range (1,n):
            q = p[:]
            q[0],q[i] = q[i], q[0]
            candidates.append(q)
    beam = sorted(candidates , key = cost)[:k]

best = min(beam,key = cost)
print("Best Tour:",best + [best[0]])
print("Minimum Distance: ",cost(best))