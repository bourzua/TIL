# def union(x, y):
#     x = find(x)
#     y = find(y)
#     if x == y:
#         return
#     elif x < y:
#         parent[y] = x
#     else:
#         parent[x] = y
#
# def find(x):
#     if x == parent[x]:
#         return x
#     parent[x] = find(parent[x])
#     return parent[x]
#
# import sys
# sys.setrecursionlimit(10**6)
#
# N = int(sys.stdin.readline())
# M = int(sys.stdin.readline())
#
# parent = [i for i in range(N+1)]
#
# # i도시의 연결정보
# for i in range(1, N+1):
#     path = list(map(int, sys.stdin.readline().split()))
#     for j in range(1, len(path)+1):
#         if path[j-1]:
#             union(i, j)
#
# tour = list(map(int, sys.stdin.readline().split()))
# check = set([find(i) for i in tour])
#
# if len(check) == 1:
#     print('YES')
# else:
#     print('NO')

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    elif x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parent = [i for i in range(N+1)]

# i도시의 연결정보
for i in range(N):
    path = list(map(int, sys.stdin.readline().split()))
    for j in range(i+1, N):
        if path[j]:
            # i, j 0부터 시작했으니까
            union(i+1, j+1)

tour = list(map(int, sys.stdin.readline().split()))
check = set([find(i) for i in tour])

if len(check) == 1:
    print('YES')
else:
    print('NO')