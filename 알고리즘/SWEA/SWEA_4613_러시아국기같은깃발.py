import sys
sys.stdin = open("4613.txt","r")

for T in range(1, int(input())+1):
    N, M = map(int, input().split())

    flag = [list((input())) for _ in range(N)]

    count = 0
    MIN = 987654321

    Wcount = 0
    for w in range(0, N-2):
        for j in range(M):
            if flag[w][j] != 'W':
                Wcount += 1
        Bcount = 0
        for b in range(w+1, N-1):
            for j in range(M):
                if flag[b][j] != 'B':
                    Bcount += 1
            Rcount = 0
            for r in range(b+1, N):
                for j in range(M):
                    if flag[r][j] != 'R':
                        Rcount += 1

            count = Wcount + Bcount + Rcount
            if MIN > count:
                MIN = count
    print("#{} {}".format(T, MIN))