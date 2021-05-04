def BFS(v):
    global ans
    visited[v] = 1
    q = deque()
    q.append(v)
    while q:
        curr = q.popleft()
        for i in graph[curr]:
            if visited[i] == 0:
                visited[i] = -visited[curr]
                q.append(i)
            elif visited[i] == visited[curr]:
                ans = 'NO'
                return

from collections import deque
import sys
N = int(sys.stdin.readline())

for _ in range(N):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    count = 0
    ans = 'YES'

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if visited[i] == 0:
            BFS(i)
    print(ans)