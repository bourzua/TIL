from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    visited[r][c] = 1
    q = deque()
    q.append((r, c, 0))



import sys

W, H = map(int, sys.stdin.readline().split())
array = [list(sys.stdin.readline().strip()) for _ in range(H)]
visited = [[0]*W for _ in range(H)]
ans = 0


for i in range(H):
    for j in range(W):
        if array[i][j] == "C":
            BFS(i, j)