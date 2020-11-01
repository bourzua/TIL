import sys
sys.setrecursionlimit(10**8)

# 미로 탈출 가능?, 최단거리 => bfs

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(i, j, power):
    global ans
    visited[i][j] = 1
    q = [(i, j, power)]

    while q:

        currI, currJ, currP = q.pop(0)

        if currI == i2 and currJ == j2:
            ans = "잘했어!!"
            return

        if currP > 0:

            for a in range(4):
                ni = currI + di[a]
                nj = currJ + dj[a]

                if nj<1 or nj>W or ni<1 or ni>H:
                    continue
                if visited[ni][nj]:
                    continue
                if miro[ni][nj] > miro[currI][currJ]:
                    if currP >= miro[ni][nj] - miro[currI][currJ]:
                        visited[ni][nj] = 1
                        q.append((ni, nj, currP - 1))

                else:
                    if currP >= 1:
                        visited[ni][nj] = 1
                        q.append((ni, nj, currP - 1))


for T in range(1, int(input())+1):
    H, W, O, F, i1, j1, i2, j2 = map(int, input().split())

    miro = [[0]*(W+1) for _ in range(H+1)]
    visited = [[0]*(W+1) for _ in range(H+1)]

    for i in range(O):
        x, y, height = map(int, input().split())
        miro[x][y] = height

    ans = '인성 문제있어??'

    bfs(i1, j1, F)

    print(ans)