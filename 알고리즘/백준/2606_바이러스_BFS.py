from collections import deque

def BFS(v):
    global cnt
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        curr_v = q.popleft()
        for i in range(1, N+1):
            if visited[i] == 0 and computer[curr_v][i] == 1:
                visited[i] = 1
                cnt += 1
                q.append(i)

N = int(input())
E = int(input())
computer = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(E):
    a, b = map(int, input().split())
    computer[a][b] = computer[b][a] = 1
cnt = 0
BFS(1)
print(cnt)