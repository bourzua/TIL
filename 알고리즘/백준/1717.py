def find(x):
    if parent[x] == x:
        return x
    # 경로 압축
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

parent = [0]*(N+1)

for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    x, a, b = map(int, sys.stdin.readline().split())
    if not x:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')