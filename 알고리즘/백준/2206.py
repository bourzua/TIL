from _collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r,c):
    visited[r][c] = 1
    q = deque()
    q.append((r, c))
    while q:
        curr_r, curr_c = q.popleft()

        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]

            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if punch[nr][nc] == 1:
                continue
            if visited[nr][nc] != 0:
                continue
            visited[nr][nc] = visited[curr_r][curr_c] + 1
            q.append((nr,nc))



N, M = map(int, input().split())

punch = [list(map(int, input())) for _ in range(N)]

distList = []
for i in range(N):
    for j in range(M):
        if punch[i][j] == 1:
            visited = [[0] * M for _ in range(N)]
            punch[i][j] = 0
            BFS(0,0)
            punch[i][j] = 1
            distList.append(visited[N-1][M-1])

if distList.count(0) == len(distList):
    print(-1)
else:
    distList.sort()
    for i in distList:
        if i > 0:
            print(i)
            break