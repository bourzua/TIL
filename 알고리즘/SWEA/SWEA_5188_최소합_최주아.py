import sys
sys.stdin = open("5188.txt", "r")

di = [0, 1]
dj = [1, 0]

def DFS(i, j, total):
    global MIN
    if total >= MIN:
        return
    if i == N-1 and j == N-1:
        if total < MIN:
            MIN = total
        return

    for a in range(2):

        ni = i + di[a]
        nj = j + dj[a]

        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        DFS(ni, nj, total + arr[ni][nj])


for T in range(1, int(input())+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    MIN = 0xfffffffff
    DFS(0, 0, arr[0][0])
    print("#{} {}".format(T, MIN))

