import sys
sys.stdin = open("4366.txt","r")

def binary(number):
    global binList
    y = int(number, 2)
    N = len(number)

    for i in range(1, N):
        ny = 0
        if number[i] == '0':
            ny = y + 2**(N-1-i)
        else:
            ny = y - 2**(N-1-i)
        binList.append(ny)

def tri(number):
    global triList
    y = int(number, 3)
    N = len(number)

    for i in range(N):
        if i == 0:
            if number[i] == '2':
                triList.append(y - 3**(N-1-i))
            else:
                triList.append(y + 3**(N-1-i))
        else:
            if number[i] == '2':
                triList.append(y - 3**(N-1-i))
                triList.append(y - 3**(N-1-i) - 3**(N-1-i))
            elif number[i] == '1':
                triList.append(y + 3**(N-1-i))
                triList.append(y - 3**(N-1-i))
            else:
                triList.append(y + 3**(N-1-i))
                triList.append(y + 3**(N-1-i) + 3**(N-1-i))



for T in range(1, int(input())+1):
    binList = []
    triList = []


    binary(input())
    tri(input())

    binList = set(binList)
    triList = set(triList)

    ans = binList & triList
    ans = list(ans)
    ans = ans[0]

    print("#{} {}".format(T, ans))
