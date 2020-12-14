import sys
sys.stdin = open("1868.txt", "r")

for T in range(1, int(input())+1):
    N = int(input())
    game = [list(input()) for _ in range(N)]

from collections import deque

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def BFS(r, c):
    # 큐에 초기값을 넣고 방문 표시
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    while queue:
        curr_r, curr_c = queue.popleft()
        for i in range(8):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                if game[nr][nc] == 0:
                    queue.append((nr, nc))


def mine_check(r, c):
    cnt = 0

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if game[nr][nc] == '*': cnt += 1

    return cnt



    zero_list =[]

    # 내 주변의 지뢰의 수로 2차원 리스트를 갱신
    for i in range(N):
        for j in range(N):
            if game[i][j] == '.':
                game[i][j] = mine_check(i, j)
            if game[i][j] == 0:
                zero_list.append((i, j))

    ans = 0 # 클릭횟수
    # 주변에 지뢰가 하나도 없는 값들을 먼저 클릭
    visited = [[False]*N for _ in range(N)]
    for r, c in zero_list:
        if visited[r][c]: continue
        BFS(r, c)
        ans += 1

    # 나머지 지뢰가 아닌 칸들을 클릭

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and game[i][j] != '*':
                ans += 1