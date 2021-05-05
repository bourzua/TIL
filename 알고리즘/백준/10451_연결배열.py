def DFS(v):
    visited[v] = 1
    if visited[list1[v]] == 0:
        DFS(list1[v])

import sys
N = int(sys.stdin.readline())

for _ in range(N):
    V = int(sys.stdin.readline())
    list1 = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0]*(V+1)
    count = 0

    for i in range(1, V+1):
        if visited[i] == 0:
            count += 1
            DFS(i)
    print(count)