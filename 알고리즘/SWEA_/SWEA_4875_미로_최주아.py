import sys
sys.stdin = open("4875.txt", "r")

di = [-1,1,0,0]
dj  =[0,0,-1,1]

def DFS(i,j):
    global result
    visited[i][j] = 1

    if arr[i][j] == 3:
        result = 1
        return


    else:
        for a in range(4):
            ni = i + di[a]
            nj = j + dj[a]

            if ni<0 or ni>=N or nj<0 or nj>=N:
                continue
            if visited[ni][nj] == 1 or arr[ni][nj] == 1:
                continue
            DFS(ni,nj)

for T in range(1, int(input())+1):
    N = int(input())
    result = 0

    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                DFS(i,j)

    print("#{} {}".format(T, result))