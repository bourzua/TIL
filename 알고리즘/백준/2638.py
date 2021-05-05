# cheese수 세기
def count(arr):
    cheese = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] == 1:
                cheese += 1
    return cheese

dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 외부공기인지 둘러쌓인 부분인지 체크 (0, 0)부터 시작
def airBFS(r, c):
    # 외부공기 체크
    paper[r][c] = 2
    q = deque()
    q.append((r,c))
    while q:
        curr_r, curr_c = q.popleft()
        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            #     근처 애들이 0이라면 외부공기
            if paper[nr][nc] == 0:
                paper[nr][nc] = 2
                q.append((nr, nc))

def cheesecheck(r, c):
    count = 0
    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if paper[nr][nc] == 2:
            count +=1
        if count >= 2:
            disappear.append((r,c))
            return



import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0

while count(paper):
    # 시간
    ans += 1
    # 외부공기 구분해주기
    airBFS(0, 0)
    # 없어질 애들 목록~
    disappear = []
    for i in range(1, N-1):
        for j in range(1, M-1):
            # 치즈면 그게 없어질 공긴지 아닌지 체크
            if paper[i][j] == 1:
                cheesecheck(i, j)
    # 없어질 치즈 하나씩 없는거로 만들어주기
    for i in disappear:
        r, c = i
        paper[r][c] = 2
print(ans)

