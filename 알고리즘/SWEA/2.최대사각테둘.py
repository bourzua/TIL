import sys
sys.stdin = open("tedoori.txt","r")

for T in range(1, int(input())+1):
    N, M, K = list(map(int, input().split()))
    rec = [list(map(int, input().split())) for _ in range(N)]


    MAX = 0
    for i in range(N - K + 1):
        for j in range(M - K + 1):
            total = 0
            for a in range(K):
                for b in range(K):
                    total += rec[i+a][j+b]

            for c in range(K-2):
                for d in range(K-2):
                    total -= rec[i+1+c][j+1+d]

            if total > MAX:
                MAX = total

    print("#{} {}".format(T, MAX))
