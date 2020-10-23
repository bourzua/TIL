import sys
sys.stdin = open("1974.txt","r")

N = int(input())
for T in range(1, N+1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]


    result = 1

    for i in range(9):
        widthList = []
        heightList = []
        for j in range(9):
            a = sudoku[i][j]
            if a in widthList:
                result = 0
                break
            widthList.append(a)

            b = sudoku[j][i]
            if b in heightList:
                result = 0
                break
            heightList.append(b)
    if result == 0:
        break

    if result == 1:
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                slashList = []
                for x in range(3):
                    for y in range(3):
                        a = sudoku[i+x][j+y]
                        if a in slashList:
                            result = 0
                            break
                        slashList.append(a)


    print("#{} {}".format(T, result))