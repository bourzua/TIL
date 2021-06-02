import sys
sys.setrecursionlimit(10**8)

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def DFS(R, C, D, fail):
    room[R][C] = '2'
    if fail == 4:
        nr = R + dr[(D+2)%4]
        nc = C + dc[(D+2)%4]
        if room[nr][nc] == 1:
            return
        else:
            DFS(nr, nc, D, 0)
    else:
        nr = R + dr[(D+3)%4]
        nc = C + dc[(D+3)%4]
        if room[nr][nc] == 0:
            DFS(nr, nc, (D+3)%4, 0)
        else:
            DFS(R, C, (D+3)%4, fail + 1)


N, M = map(int, input().split())
r, c, d =  map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
DFS(r, c, d, 0)
count = 0
for i in range(N):
    for j in range(M):
        if room[i][j] == '2':
            count += 1
print(count)