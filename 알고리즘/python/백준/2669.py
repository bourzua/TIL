list = [[0]*100 for _ in range(100)]


for i in range(4):
    x, y, p, q = map(int, input().split())

    for a in range(x, p):
        for b in range(y, q):
            list[a][b] = 1

area = 0
for i in range(100):
    for j in range(100):
        if list[i][j]==1:
            area += 1

print(area)