import sys
sys.stdin = open("1248.txt","r")

def findP(x,y):
    pofX = [1]
    pofY = [1]

    while x>1:
        for i in range(1, V+1):
            if x in arr[i]:
                pofX.append(i)
        x = i

    while y>1:
        for i in range(1, V+1):
            if y in arr[i]:
                pofY.append(i)
        y = i

    common = [val for val in pofX if val in pofY]

    return common



for T in range(1, int(input())+1):
    V, E, A, B = map(int, input().split())
    path = list(map(int, input().split()))

    arr = [[] for _ in range(V+1)]
    # print(arr)

    for i in range(V-1):
        p, c = path[2*i], path[2*i+1]
        arr[p].append(c)

    commonList = findP(A,B)

    common = max(commonList)
    print(common)