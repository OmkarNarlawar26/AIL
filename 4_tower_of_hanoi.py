def hanoi(n,source,auxiliary,destination):
    if n == 1:
        print(source,"->",destination)
        return
    hanoi(n-1,source,destination,auxiliary)
    print(source,"->",destination)
    hanoi(n - 1,auxiliary,source,destination)

n = 3
hanoi(n,'A','B','C')