import sys
sys.stdin = open("4835.txt","r")

for T in range(1, int(input())+1):
    N, M = map(int, input().split())

    numberList = list(map(int, input().split()))
    
    totalList =[]

    for i in range(N-M+1):
        total = 0
        for j in range(M):
            total += numberList[i+j]
        totalList.append(total)

    MAX = max(totalList)
    MIN = min(totalList)

    print("#{} {}".format(T, MAX-MIN))