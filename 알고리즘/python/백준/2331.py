def DFS(a, p):
    global start
    next = 0
    a = str(a)
    for i in range(len(a)):
        next += int(a[i])**p
    if next in visited:
        start = next
        return
    else:
        visited.append(next)
        DFS(next, p)

import sys

A, P = map(int,sys.stdin.readline().split())
visited = [A]
start = 0
count = 0

DFS(A,P)

for i in visited:
    if i == start:
        break
    count += 1

print(count)