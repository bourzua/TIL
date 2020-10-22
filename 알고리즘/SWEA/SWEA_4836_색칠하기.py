import sys
sys.stdin = open("4836.txt","r")

for T in range(1, int(input())+1):
    N = int(input())

    paper = [[0]*10 for _ in range(10)]

    for _ in range(N):
        a, b, c, d, e = map(int, input().split())
        for i in range(a, c+1):
            for j in range(b, d+1):
                if paper[i][j] == 0 or paper[i][j] == e:
                    paper[i][j] = e
                else:
                    paper[i][j] += e

    count = 0
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 3:
                count += 1

    print(f"#{T} {count}".format())
