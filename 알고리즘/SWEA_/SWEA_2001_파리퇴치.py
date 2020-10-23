import sys
sys.stdin = open("2001.txt","r")

for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    window = [list(map(int, input().split())) for _ in range(N)]
    totalList = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for a in range(M):
                for b in range(M):
                    total += window[i+a][j+b]
            totalList.append(total)

    MAX = max(totalList)

    print("#{} {}".format(T, MAX))