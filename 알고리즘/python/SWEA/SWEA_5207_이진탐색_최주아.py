import sys
sys.stdin = open("5207.txt","r")

def binSearch():
    result = 0
    for b in B:
        before, tmp = '', ''
        l = 0
        r = N - 1
        while l <= r:
            m = (l + r) // 2
            if b == A[m]:
                result += 1
                break
            elif b < A[m]:
                r = m - 1
                tmp = 'left'
            elif b > A[m]:
                l = m + 1
                tmp = 'right'
            if before == tmp:
                break
            before = tmp
    return result

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    print("#{} {}".format(T, binSearch()))