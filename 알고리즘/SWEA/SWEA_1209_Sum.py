import sys
sys.stdin = open("1209.txt","r")

for T in range(1, 11):
    number = int(input())
    puzzle = [list(map(int, input().split())) for _ in range(100)]
    sumList =[]

    for i in range(100):
        SUM = 0
        SUM2 = 0
        for j in range(100):
            SUM += puzzle[i][j]
            SUM2 += puzzle[j][i]

        oneOfTwo = max(SUM,SUM2)
        sumList.append(oneOfTwo)
    SUM3 = 0
    SUM4 = 0
    for i in range(100):
        SUM3 += puzzle[i][i]
    for i in range(100):
        SUM4 = puzzle[i][99-i]

    sumList.append(SUM3)
    sumList.append(SUM4)

    realMax = max(sumList)

    print("#{} {}".format(T, realMax))