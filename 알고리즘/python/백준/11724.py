def DFS(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            DFS(i)

import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
count = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    if visited[i] == 0:
        count += 1
        DFS(i)
print(count)