dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, num):

    if len(num) == 6:
        number.add(num)
        return

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]

        if nr >= 5 or nr < 0 or nc >= 5 or nc < 0:
            continue
        dfs(nr, nc, num + numpad[nr][nc])

import sys
numpad = [list(sys.stdin.readline().split()) for _ in range(5)]
number = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, numpad[i][j])
print(len(number))