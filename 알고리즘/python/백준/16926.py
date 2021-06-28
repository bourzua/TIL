N, M, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
rotateNum = min(N,M)//2
groups = []

for k in range(rotateNum):
    group = []
    for j in range(k, M-k):
        group.append(a[k][j])
    for i in range(k+1, N-k-1):
        group.append(a[i][M-1-k])
    for j in range(M-1-k, k, -1):
        group.append(a[N-1-k][j])
    for i in range(N-1-k, k, -1):
        group.append(a[i][k])
    groups.append(group)

for k in range(rotateNum):
    group = groups[k]
    l = len(group)
    index = R%l
    for j in range(k, M-k):
        a[k][j] = group[index]
        index = (index+1)%l
    for i in range(k + 1, N - k - 1):
        a[i][M - 1 - k] = group[index]
        index = (index + 1) % l
    for j in range(M-1-k, k, -1):
        a[N-1-k][j] = group[index]
        index = (index + 1) % l
    for i in range(N-1-k, k, -1):
        a[i][k] = group[index]
        index = (index + 1) % l

for row in a:
    print(*row, sep=' ')