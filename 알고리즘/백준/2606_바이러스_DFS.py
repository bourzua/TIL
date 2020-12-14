def DFS(v):
    global cnt
    visited[v] = 1
    for i in range(1, N+1):
        if visited[i] == 0 and computer[v][i] == 1:
            cnt += 1
            DFS(i)

N = int(input())
E = int(input())
computer = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(E):
    a, b = map(int, input().split())
    computer[a][b] = computer[b][a] = 1
cnt = 0
DFS(1)
print(cnt)