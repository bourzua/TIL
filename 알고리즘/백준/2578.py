def countbingo(v):
    global countList
    a = b = 0
    flag = True
    for i in range(5):
        for j in range(5):
            if arr[i][j] == v:
                a = i
                b = j
                flag = False
                break
        if flag == False: break

    countList[a] += 1
    countList[5+b] += 1
    if a == 2 and b == 2:
        countList[10] += 1
        countList[11] += 1
    if a == b and a!=2 and b!=2:
        countList[10] += 1
    if a + b == 4 and a!=2 and b!=2:
        countList[11] += 1
    return

arr = [list(map(int, input().split())) for _ in range(5)]


countList = [0]*12

given = [list(map(int, input().split())) for _ in range(5)]


count = 0
flag2 = True
for i in range(5):
    for j in range(5):
        count += 1
        a = given[i][j]
        countbingo(a)

        if countList.count(5) >= 3:
            print(count)
            flag2 = False
            break
    if flag2 == False: break