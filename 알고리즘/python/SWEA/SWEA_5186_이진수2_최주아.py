import sys
sys.stdin = open("5186.txt","r")

for T in range(1, int(input())+1):
    N = float(input())

    binList = ''
    # 1/2로 나누고 1/4로 나누고 ...
    i = -1
    while N>0:
        if i == -13:
            binList = 'overflow'
            break
        a = N // 2**i
        binList += str(int(a))
        N -= a*(2**i)
        i -= 1

    print("#{} {}".format(T, binList))