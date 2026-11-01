# Implement Local Beam Search for The Traveling Salesman Problem (TSP).

import random

dist = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]

def cost(path):
    total = 0
    for i in range(len(path)):
        total += dist[path[i]][path[(i + 1) % len(path)]]
    return total

n = 4
k = 3

beam = [random.sample(range(n), n) for _ in range(k)]

for _ in range(50):
    new_beam = []

    for path in beam:
        for i in range(1, n):
            new_path = path[:]
            new_path[0], new_path[i] = new_path[i], new_path[0]
            new_beam.append(new_path)

    beam = sorted(new_beam, key=cost)[:k]

best = min(beam, key=cost)

print("Best Tour:", [x + 1 for x in best + [best[0]]])
print("Minimum Distance:", cost(best))