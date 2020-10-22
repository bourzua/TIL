import sys
sys.stdin = open("1959.txt","r")

for T in range(1, int(input())+1):
    M, N = map(int, input().split())

    more = max(M,N)
    less = min(M,N)

    print(more, less)

    listA = list(map(int, input().split()))
    listB = list(map(int, input().split()))

    totalList = []
    total = 0

    if len(listA) > len(listB):
        for i in range(-----:
            for j in range(more-less+1):
                total += listB[i]*listA[i+j]
            totalList.append(total)

    else:
        for i in range(less):
            for j in range(more-less+1):
                total += listA[i]*listB[i+j]
            totalList.append(total)

    answer = max(totalList)

    print("#{} {}".format(T, answer))
