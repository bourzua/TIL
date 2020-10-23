import sys
sys.stdin = open("1861.txt","r")

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def DFS(r,c):
    global count

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0<=nr<N and 0<=nc<N and rec[nr][nc]-rec[r][c] == 1:
            count +=1
            DFS(nr,nc)

for T in range(1, int(input())+1):
    N = int(input())

    rec = [list(map(int, input().split())) for _ in range(N)]

    countArr = [[0]*N for _ in range(N)]


    for i in range(N):
        for j in range(N):
            count = 1
            DFS(i,j)
            countArr[i][j] = count

    MAX = 0
    for i in range(N):
        for j in range(N):
            if countArr[i][j] > MAX:
                MAX = countArr[i][j]
    minList = []
    for i in range(N):
        for j in range(N):
            if countArr[i][j] == MAX:
                minList.append(rec[i][j])

    print("#{} {} {}".format(T, min(minList), MAX))