# pypy로 해야 돌아감

# 연결리스트 사용
def DFS(v):
    global visited
    # 방문 표시
    visited[v] = 1
    # 연결된 노드가 있다면
    if len(graph[v]):
        for i in range(len(graph[v])):
            if visited[graph[v][i]] == 0:
                DFS(graph[v][i])

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

# 정점 하나도 연결요소로 친다.
for i in range(1, N+1):
    if visited[i] == 0:
        count += 1
        DFS(i)

print(count)