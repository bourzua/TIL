import sys
sys.setrecursionlimit(10**8)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def DFS(r, c):
    visited[r][c] = 1

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if nr<0 or nr>=N or nc<0 or nc>=N:
            continue
        if visited[nr][nc]:
            continue
        if height[nr][nc] <= i:
            continue
        DFS(nr, nc)

N = int(input())
height = [list(map(int, input().split())) for _ in range(N)]
MAX = 0
MIN = 0xfffffffff
for i in range(N):
    for j in range(N):
        if height[i][j] > MAX:
            MAX = height[i][j]
        if height[i][j] < MIN:
            MIN = height[i][j]
# *****
# 제일 낮은 지역보다 낮게 오면 항상 1개니까
safezoneMAX = 1
for i in range(MIN, MAX):
    visited = [[0]*N for _ in range(N)]
    count = 0
    for j in range(N):
        for k in range(N):
            if height[j][k] <= i:
                continue
            if visited[j][k]:
                continue
            count += 1
            DFS(j, k)
    if count > safezoneMAX:
        safezoneMAX = count
print(safezoneMAX)