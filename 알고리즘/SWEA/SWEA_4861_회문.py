import sys
sys.stdin = open("4861.txt","r")

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    result = ''

    rec = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            words = ''
            for a in range(M):
                words += rec[i][j+a]
            if words == words[::-1]:
                result = words

    for i in range(N-M+1):
        for j in range(N):
            words = ''
            for a in range(M):
                words += rec[i+a][j]
            if words == words[::-1]:
                result = words

    print("#{} {}".format(T, result))