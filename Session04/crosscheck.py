l = [0, 1, 2, 3, 4]
n = len(l)
for i in range(n - 1):
    for j in range(i+1, n):
        print(i, "vs", j)
