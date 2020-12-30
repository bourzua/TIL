import sys
sys.stdin = open("1211.txt", "r")

di = [0, 0, 1]
dj = [-1, 1, 0]

def DFS(i, j, k):
    global cnt, min_cnt, ans
    visited[i][j] = 1
    for a in range(3):
        ni = i + di[a]
        nj = j + dj[a]
        if ni<0 or ni>=100 or nj<0 or nj>=100:
            continue
        if visited[ni][nj] == 1:
            continue
        if ladder[ni][nj] == 0:
            continue
        if ni == 99:
            cnt += 1
            min_cnt = cnt
            ans = k
            return
        else:
            if a == 0 or a == 1:
                visited[i+1][j] = 1
                cnt += 1
            if cnt >= min_cnt:
                return
            DFS(ni, nj, k)

for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    startlist = []
    for i in range(100):
        if ladder[0][i] == 1:
            startlist.append((0, i))
    lenList = []
    ans = 0
    min_cnt = 0xffffff
    for i in startlist:
        visited = [[0]*100 for _ in range(100)]
        cnt = 0
        r, c = i
        DFS(r, c, c)
    print("#{} {}".format(T, ans))