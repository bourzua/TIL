import sys
sys.stdin = open("color.txt","r")

for T in range(1, int(input())+1):
    N, M = map(int, input().split())


    paper = [[0]*N for i in range(N)]

    for i in range(M):
        a,b,c,d = map(int, input().split())
        for i in range(a, c+1):
            for j in range(b, d+1):
                paper[i][j] = 1

    count = 0
    for i in range(N):
        for j in range(N):
            if paper[i][j] == 1:
                count += 1

    print("#{} {}".format(T, count))