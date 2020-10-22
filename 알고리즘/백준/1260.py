def DFS(Z):
    global DFS_path
    global visited
    visited[Z] = 1
    DFS_path += str(Z) + ' '
    for i in range(1, N+1):
        if arr[Z][i] == 1 and visited[i] == 0:
            DFS(i)

def BFS(Z):
    global visited
    global BFS_path
    visited[Z] = 1
    q = [Z]
    while q:
        curr = q.pop(0)
        BFS_path += str(curr) + ' '
        for i in range(1, N+1):
            if arr[curr][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)

N, M, V = map(int, input().split())

arr = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1
DFS_path = ''
BFS_path = ''
DFS(V)
visited = [0]*(N+1)
BFS(V)
print(DFS_path)
print(BFS_path)