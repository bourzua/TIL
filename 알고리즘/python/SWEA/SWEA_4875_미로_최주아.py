import sys
sys.stdin = open("4875.txt", "r")

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    global ans
    q = deque()
    q.append((r, c))
    while q:
        curr_r, curr_c = q.popleft()
        visited[curr_r][curr_c] = 1

        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]

            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if visited[nr][nc] == 1:
                continue
            if miro[nr][nc] == 0:
                q.append((nr, nc))
            if miro[nr][nc] == 3:
                ans = 1
                return

for T in range(1, int(input())+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                BFS(i, j)
    print("#{} {}".format(T, ans))