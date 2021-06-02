import sys
sys.stdin = open("10726.txt", "r")

for T in range(1, int(input())+1):
    N, M = map(int, input().split())

    ans = "OFF"

    for i in range(N):
        if (M & (1 << i)) == 0:
            break
        if i == N-1:
            ans = "ON"

    print("#{} {}".format(T, ans))