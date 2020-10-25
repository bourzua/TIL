def DFS(v):
    global dfsPath
    dfsPath.append(v)
    visited[v] = 1

    if len(graph[v]):
        for i in range(len(graph[v])):
            if visited[graph[v][i]] == 0:
                DFS(graph[v][i])

def BFS(v):
    global bfsPath
    global visited
    q = [v]
    bfsPath.append(v)
    visited[v] = 1
    while q:
        curr = q.pop(0)
        for i in range(len(graph[curr])):
            if visited[graph[curr][i]] == 0:
                visited[graph[curr][i]] = 1
                q.append(graph[curr][i])
                bfsPath.append(graph[curr][i])

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
# 연결 방식: 1. 연결리스트
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

dfsPath = []
bfsPath = []

DFS(V)
visited = [0]*(N+1)
BFS(V)
print(*dfsPath)
print(*bfsPath)