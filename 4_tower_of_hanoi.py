# Implement Tower of Hanoi by State Space Search

step = 1

def hanoi(n, source, auxiliary, destination):
    global step

    if n == 1:
        print("Step", step, ":", source, "->", destination)
        step += 1
        return

    hanoi(n - 1, source, destination, auxiliary)

    print("Step", step, ":", source, "->", destination)
    step += 1

    hanoi(n - 1, auxiliary, source, destination)


n = 3
hanoi(n, 'A', 'B', 'C')