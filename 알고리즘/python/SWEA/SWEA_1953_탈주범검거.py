import sys
sys.stdin = open("1953.txt", "r")

from collections import deque

di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]
info = [[],[0,1,2,3],[0,1],[2,3],[0,3],[1,3],[1,2],[0,2]]


def go(r, c, l):
    q = deque()
    q.append((r,c,l-1))
    visited[r][c] = 1

    while q:
        i, j, time = q.popleft()

        if time == 0:
            continue
        else:

            k = tunnel[i][j]

            for a in info[k]:
                ni = i + di[a]
                nj = j + dj[a]

                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                if tunnel[ni][nj] == 0:
                    continue
                if visited[ni][nj]:
                    continue
                if a == 0 and (tunnel[ni][nj] == 3 or tunnel[ni][nj] == 4 or tunnel[ni][nj] == 7):
                    continue
                if a == 1 and (tunnel[ni][nj] == 3 or tunnel[ni][nj] == 5 or tunnel[ni][nj] == 6):
                    continue
                if a == 2 and (tunnel[ni][nj] == 2 or tunnel[ni][nj] == 6 or tunnel[ni][nj] == 7):
                    continue
                if a == 3 and (tunnel[ni][nj] == 2 or tunnel[ni][nj] == 4 or tunnel[ni][nj] == 5):
                    continue

                visited[ni][nj] = 1
                q.append((ni, nj, time-1))


for T in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())

    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    count = 0
    go(R, C, L)

    count = 0


    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                count += 1

    print("#{} {}".format(T, count))