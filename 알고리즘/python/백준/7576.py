from _collections import deque

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

q = deque()

for i in range(N):
    for j in range(M):
         if tomato[i][j] == 1:
             q.append((i,j))

numberOfStart = len(q)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

while q:
    r,c = q.popleft()

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]

        if nr<0 or nr>=N or nc<0 or nc>=M:
            continue
        if tomato[nr][nc] == -1 or tomato[nr][nc] == 1:
            continue
        if visited[nr][nc] != 0:
            continue
        tomato[nr][nc] = 1
        visited[nr][nc] = visited[r][c] + 1
        q.append((nr, nc))

MAX = 0
ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] > MAX:
            MAX = visited[i][j]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            MAX = -1

print(MAX)