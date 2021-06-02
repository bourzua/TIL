import sys
N = int(sys.stdin.readline())
for _ in range(N):
    numList = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(1, len(numList)-1):
        for j in range(i+1, len(numList)):
            a = numList[i]
            b = numList[j]
            while b:
                a,b=b,a%b
            ans += a
    print(ans)
