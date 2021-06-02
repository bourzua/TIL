import sys

def Goldbach():
    e = [False, False] + [True]*(1000000-1)
    for i in range(2, 1001):
        if e[i]:
            for j in range(i+i, 1000001, i):
                e[j] = False


    while True:
        N = int(sys.stdin.readline())
        flag = 0

        if N == 0:
            break

        for i in range(2, N//2 + 1):
            if e[i] and e[N-i]:
                print("{} = {} + {}".format(N, i, N-i))
                flag = 1
                break
        if flag == 0:
            print("Goldbach's conjecture is wrong.")

Goldbach()