from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited = [0]*(N + 1)
    visited[v] = 1
    cnt = 1
    while q:
        curr_v = q.popleft()
        for a in computers[curr_v]:
            if visited[a] == 0:
                visited[a] = 1
                cnt += 1
                q.append(a)
    return cnt

import sys
N, M = map(int, sys.stdin.readline().split())

computers = [[] for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    computers[B].append(A)

noc = []
max = 0
for i in range(1, N + 1):
    tmp = bfs(i)
    if max == tmp:
        noc.append(i)
    if max < tmp:
        noc = []
        max = tmp
        noc.append(i)

print(*noc)