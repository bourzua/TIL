import sys
sys.stdin = open('input.txt',"r")

di = [0, 0,1]
dj = [-1,1,0]

def check(i,j):
    visited[i][j] = 1

    if ladder[i][j] == 2:
        return True
    elif i == 99:
        return False
    else:
        for d in range(3):
            ni, nj = i + di[d], j + dj[d]
            if (0 <= ni < 100) and (0 <= nj < 100) and ladder[ni][nj] != 0 and visited[ni][nj] == 0:
                return  check(ni,nj)

for _ in range(10):
    T = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    start = []
    for j in range(100):
        if ladder[0][j] == 1:
            start.append(j)

    for s in start:
        visited = [[0]*100 for _ in range(100)]

        if check(0,s):
            print("#{} {}".format(T,s))
            break