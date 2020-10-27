import sys
sys.stdin = open("5186.txt","r")

for T in range(1, int(input())+1):
    N = float(input())

    binList = ''
    i = -1
    while N>0:
        if i == -14:
            binList = 'overflow'
            break
        a = N // 2**i
        binList += str(int(a))
        N -= a*(2**i)
        i -=1

    print("#{} {}".format(T, binList))