import sys
sys.stdin = open("2805.txt","r")

for T in range(1,int(input())+1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    center = N//2
    total = 0

    for i in range(N):
        if i <= center:
            for j in range(center-i, center+i+1):
                total += arr[i][j]
        else:
            for j in range(i-center, N+center-i):
                total += arr[i][j]

    print("#{} {}".format(T, total))