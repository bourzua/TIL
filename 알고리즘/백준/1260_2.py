# 인접리스트

def DFS(v):
    dfsList.append(v)
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            DFS(i)

def BFS(v):
    bfsList.append(v)
    visited[v] = 1
    q = [v]

    while q:
        curr = q.pop(0)
        for i in graph[curr]:
            if visited[i] == 0:
                visited[i] = 1
                bfsList.append(i)
                q.append(i)



import sys
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
dfsList = []
bfsList = []


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

DFS(V)
visited = [0]*(N+1)
print(*dfsList)
BFS(V)
print(*bfsList)