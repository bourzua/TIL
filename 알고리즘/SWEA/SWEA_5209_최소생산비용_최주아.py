import sys
sys.stdin = open("5209.txt", "r")

def minimumP(a, c):
    global MIN
    if c >= MIN:
        return
    if a == N:
        if c < MIN:
            MIN = c
        return
    for i in range(N):
        if not idx[i]:
            idx[i] = 1
            minimumP(a + 1, c + cost[a][i])
            idx[i] = 0


for T in range(1,int(input())+1):
    N = int(input())

    cost = [list(map(int, input().split())) for _ in range(N)]
    idx = [0]*N

    MIN = 0xfffffff
    minimumP(0, 0)

    print("#{} {}".format(T, MIN))