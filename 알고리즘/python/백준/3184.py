dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

from collections import deque

def bfs(r, c):
    global s, w
    visited[r][c] = 1
    q = deque()
    q.append((r, c))
    if field[r][c] == "o":
        s += 1
    elif field[r][c] == "v":
        w += 1

    while q:
        curr_r, curr_c = q.popleft()

        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]

            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0 and field[nr][nc] != "#":
                if field[nr][nc] == "o": s += 1
                if field[nr][nc] == "v": w += 1
                visited[nr][nc] = 1
                q.append((nr, nc))


import sys
R, C = map(int, sys.stdin.readline().split())

# field = [list(sys.stdin.readline().strip()) for _ in range(C)]
field = []
visited = [[0]*C for _ in range(R)]

sheep = 0
wolf = 0

for i in range(R):
    a = list(sys.stdin.readline().strip())
    for j in range(C):
        if a[j] == "o": sheep += 1
        if a[j] == "v": wolf += 1
    field.append(a)

for i in range(R):
    for j in range(C):
        if field[i][j] != "#" and field[i][j] != "." and visited[i][j] == 0:
            s, w = 0, 0
            bfs(i, j)
            if s > w:
                wolf -= w
            else:
                sheep -= s

print(sheep, wolf)