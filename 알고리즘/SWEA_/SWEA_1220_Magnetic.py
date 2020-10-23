import sys
sys.stdin = open("1220.txt","r")

def DFS(i,j):
    global count

    if i == 99:
        return count

    else:
        ni = i + 1
        nj = j

        if arr[ni][nj] == 2:
            count += 1
            return count
        elif arr[ni][nj] ==1:
            return count
        elif arr[ni][nj] == 0:
            DFS(ni,nj)

for T in range(1, 11):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                DFS(i,j)

    print("#{} {}".format(T, count))