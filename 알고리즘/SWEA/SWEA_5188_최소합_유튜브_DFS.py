# 꼭 델타이동을 써야하는 것은 아님!

import sys
sys.stdin = open("5188.txt", "r")

for T in range(1, int(input())+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0xfffffff
    def dfs(x, y, dist):
        global ans
        if dist >= ans:
            return
        if x == N - 1 and y == N - 1:
            ans = min(ans, dist)
        else:
            if x + 1 < N:
                dfs(x+1, y, dist + arr[x+1][y])
            if y + 1 < N:
                dfs(x, y+1, dist + arr[x][y+1])
    dfs(0, 0, arr[0][0])
    print("#{} {}".format(T, ans))

