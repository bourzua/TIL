import sys
sys.stdin = open("4831.txt","r")

for T in range(1, int(input())+1):
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))
    now = 0
    count = 0

    while now < N - K:
        move = []
        for i in range(1, K+1):
            if now + i in charge:
                move.append(i)
        if len(move)>0:
            a = max(move)
            now += a
            count += 1
        else:
            count = 0
            break


    print("#{} {}".format(T, count))