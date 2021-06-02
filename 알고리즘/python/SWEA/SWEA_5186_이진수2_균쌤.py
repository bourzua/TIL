import sys
sys.stdin = open("5186.txt","r")

for T in range(1, int(input())+1):
    N = float(input())
    ans = ''

    while True:
        N *= 2
        ans += str(N)[0]
        if N >= 1: N -= 1
        if N == 0:
            break

        if len(ans) >= 13:
            ans = 'overflow'
            break

    print("#{} {}".format(T, ans))