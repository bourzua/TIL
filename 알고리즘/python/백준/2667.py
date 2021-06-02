#BFS

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    global count
    visited[r][c] = 1
    q = [(r,c)]
    while q:
        curr_r, curr_c = q.pop(0)
        count += 1
        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))

import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))
visited = [[0]*N for _ in range(N)]
numberOfHouse = []
totalCount = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and arr[i][j] == 1:
            totalCount += 1
            count = 0
            BFS(i, j)
            numberOfHouse.append(count)

numberOfHouse.sort()
print(totalCount)
for i in numberOfHouse:
    print(i)
