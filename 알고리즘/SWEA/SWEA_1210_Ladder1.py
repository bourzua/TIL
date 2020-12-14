import sys
sys.stdin = open('1210.txt',"r")
# 반대로 생각
# 목적지에서 출발지로 올라간다고 생각하면 1가지 경로만 탐색해도 됨

# 좌, 우, 상
di = [0, 0, -1]
dj = [-1, 1, 0]

def DFS(i, j):
    global ans
    visited[i][j] = 1
    # 좌우상만 보기
    for a in range(3):
        ni = i + di[a]
        nj = j + dj[a]
        if ni<0 or ni>=100 or nj<0 or nj>=100:
            continue
        if ladder[ni][nj] == 0:
            continue
        if visited[ni][nj] == 1:
            continue
        # 좌나 우로 가게된다면 그 위좌표는 못가게 막기
        if a == 0 or a == 1:
            visited[i-1][j] = 1
        # new좌표의 행이 0이면 열은 정답!
        if ni == 0:
            ans = nj
            return
        DFS(ni, nj)

for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]
    ans = 0
    # 2인 좌표 찾기
    r = c = 0
    for i in range(100):
        if ladder[99][i] == 2:
            r, c = 99, i
    # 탐색 시작
    DFS(r, c)
    print("#{} {}".format(T, ans))