def DFS(v, path):
    global teamCount
    visited[v] = 1
    path.append(v)
    if want[v] in path:
        if path.index(want[v]) == 0:
            teamCount += len(path)
            return
        else:
            teamCount += (len(path) - path.index(want[v]))
            return
    if visited[want[v]]:
        return
    DFS(want[v], path)

import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    teamCount = 0
    visited = [0]*(N+1)
    want = [0] + list(map(int, sys.stdin.readline().split()))

    for i in range(1, N+1):
        if want[i] == i:
            teamCount += 1
            visited[i] = 1

    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        if visited[want[i]]:
            continue
        path = [i]
        DFS(want[i], path)

    print(N - teamCount)