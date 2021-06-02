def bfs():
    while q:
        x, y = q.popleft()
        z = C - x - y

        if x == 0:
            zList.append(z)
        # x -> y
        water = min(x, B - y)
        visitCheck(x - water, y + water)
        # x -> z
        water = min(x, C - z)
        visitCheck(x - water, y)
        # y -> x
        water = min(y, A - x)
        visitCheck(x + water, y - water)
        # y -> z
        water = min(y, C - z)
        visitCheck(x, y - water)
        # z -> x
        water = min(z, A - x)
        visitCheck(x + water, y)
        # z -> y
        water = min(z, B - y)
        visitCheck(x, y + water)



def visitCheck(x, y):
    if visited[x][y] == 0:
        visited[x][y] = 1
        q.append((x, y))


from collections import deque
import sys

A, B, C = map(int, sys.stdin.readline().split())
visited = [[0]*(B+1) for _ in range(A+1)]
zList = []

q = deque()
visited[0][0] = 1
q.append((0, 0))

bfs()
zList = sorted(zList)

for i in zList:
    print(str(i), end=" ")