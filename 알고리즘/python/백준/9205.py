def DFS(v):
    global ans
    visited[v] = 1
    if v == N + 1:
        ans = 'happy'
    for i in range(N+2):
        if abs(cass[v][0] - cass[i][0]) + abs(cass[v][1] - cass[i][1]) <= 1000 and visited[i] == 0:
            DFS(i)

for T in range(1, int(input())+1):
    N = int(input())
    cass = []
    for _ in range(N+2):
        a, b = map(int, input().split())
        cass.append((a, b))
    visited = [0]*(N+2)
    ans = 'sad'
    DFS(0)
    print(ans)