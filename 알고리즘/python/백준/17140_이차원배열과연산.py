def R():
    arr = [[] for _ in range(len(A))]
    for i in range(3):
        check = [0]*101
        for j in range(len(A[i])):
            p = A[i][j]
            check[p] += 1
        for x in range(len(check)):
            if check[x]:
                arr[i].append((x, check[x]))
    for i in range(len(arr)):
        arr[i] = sorted(arr[i], key=lambda x:(x[1],x[0]))
    realArr = [[] for _ in range(len(A[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            realArr[i].append(arr[i][j][0])
            realArr[i].append(arr[i][j][1])
    maxLen = 0
    for i in range(len(realArr)):
        if len(realArr[i]) > maxLen:
            maxLen = len(realArr[i])
    for i in range(len(realArr)):
        if len(realArr[i]) < maxLen:
            for j in range(maxLen-len(realArr[i])):
                realArr[i].append(0)
    return realArr

def firstCircle():
    r, c = len(A), len(A[0])
    arr = [[] for _ in range(c)]
    for i in range(c):
        for j in range(r, -1, -1):
            print(i,j)
            arr[i].append(A[i][j])
    return arr

def secondCircle():
    r, c = len(A), len(A[0])
    arr = [[] for _ in range(c)]
    for i in range(c-1, -1, -1):
        for j in range(r):
            print(i,j)
            arr[c-i-1].append(A[j][i])
    return arr

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
time = 0
N = len(A)
M = len(A[0])
while A[r-1][c-1] != k:
    if time == 100:
        print(-1)
        break
    if len(A) >= len(A[0]):
        A = R()
    else:
        [print(_a) for _a in A]
        print()
        A = firstCircle()
        R()
        A = secondCircle()
    time += 1
    
print(time)