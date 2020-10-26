import sys
sys.setrecursionlimit(10**6)

# 상하좌우, 좌상, 우상, 좌하, 우하
di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

def DFS(i, j):

    visited[i][j] = 1

    for a in range(8):

        ni = i + di[a]
        nj = j + dj[a]

        if ni<0 or ni>=h or nj<0 or nj>=w:
            continue
        if island[ni][nj] == 0 or visited[ni][nj] != 0:
            continue
        DFS(ni,nj)


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    island = []
    for i in range(h):
        island.append(list(map(int,input().split())))

    visited = [[0]*w for _ in range(h)]

    count = 0

    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and island[i][j] == 1:
                DFS(i,j)
                count += 1

    print(count)