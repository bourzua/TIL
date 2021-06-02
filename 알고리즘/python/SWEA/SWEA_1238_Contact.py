import sys
sys.stdin = open("1238.txt","r")

for T in range(1,11):
    N, s = map(int, input().split())

    pathList = list(map(int, input().split()))

    G = [[0] * 101 for _ in range(101)]
    visited = [0] * 101

    for i in range(0,N,2):
        G[pathList[i]][pathList[i+1]] = 1

    Q = [s]
    visited[s] = 1

    while Q:
        v = Q.pop(0)
        for i in range(101):
            if G[v][i] == 1 and visited[i] == 0:
                visited[i] = visited[v] + 1
                Q.append(i)
    ans = 1
    for i in range(2, 101):
        if visited[ans] <= visited[i]:
            ans = i

    print("#{} {}".format(T, ans))