import sys
sys.stdin = open("4881.txt", "r")

def perm(k, cur_sum):
    global ans
    if cur_sum >= ans:
        return
    if k == N:
        ans = min(ans, cur_sum)
    else:
        for i in range(k, N):
            cols[k], cols[i] = cols[i], cols[k]
            perm(k+1, cur_sum + arr[k][cols[k]])
            cols[k], cols[i] = cols[i], cols[k]

for T in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cols = [i for i in range(N)]
    ans = 0xffffff
    perm(0, 0)
    print("#{} {}".format(T, ans))

