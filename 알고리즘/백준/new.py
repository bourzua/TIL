def BFS(v):
    global ans
    visited[v] = 1
    q = [v]
    while q:
        curr = q.pop(0)
        for i in graph[curr]:
            if visited[i] == 0:
                if visited[curr] == 1:
                    visited[i] = 2
                elif visited[curr] == 2:
                    visited[i] = 1
                q.append(i)
            elif visited[i] == visited[curr]:
                ans = 'NO'
                return

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