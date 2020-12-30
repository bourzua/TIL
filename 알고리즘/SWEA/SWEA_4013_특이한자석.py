import sys
sys.stdin = open("4013.txt","r")

def clock(a, dir):
    if dir == 1:
        new = magnet[a].pop()
        magnet[a].insert(0, new)
    elif dir == -1:
        new = magnet[a].pop(0)
        magnet[a].append(new)
def rotate(i, j):
    if i == 1 or i == 3:
        li = [0] + [j, j*(-1), j, j*(-1)]
    else:
        li = [0] + [j*(-1), j, j*(-1), j]
    yesOrNo = [0]*5
    yesOrNo[i] = 1
    if i == 1:
        if magnet[i][2] != magnet[i+1][6]:
            yesOrNo[i+1] = 1
            if magnet[i+1][2] != magnet[i+2][6]:
                yesOrNo[i+2] = 1
                if magnet[i+2][2] != magnet[i+3][6]:
                    yesOrNo[i+3] = 1
    elif i == 2:
        if magnet[i-1][2] != magnet[i][6]:
            yesOrNo[i-1] = 1
        if magnet[i][2] != magnet[i+1][6]:
            yesOrNo[i+1] = 1
            if magnet[i+1][2] != magnet[i+2][6]:
                yesOrNo[i+2] = 1
    elif i == 3:
        if magnet[i-1][2] != magnet[i][6]:
            yesOrNo[i-1] = 1
            if magnet[i-2][2] != magnet[i-1][6]:
                yesOrNo[i-2] = 1
        if magnet[i][2] != magnet[i + 1][6]:
            yesOrNo[i+1] = 1
    elif i == 4:
        if magnet[i-1][2] != magnet[i][6]:
            yesOrNo[i-1] = 1
            if magnet[i-2][2] != magnet[i-1][6]:
                yesOrNo[i-2] = 1
                if magnet[i-3][2] != magnet[i-2][6]:
                    yesOrNo[i-3] = 1
    for i in range(1, 5):
        if yesOrNo[i] == 1:
            clock(i, li[i])

for T in range(1, int(input())+1):
    K = int(input())
    magnet =[0]
    for _ in range(4):
        magnet.append(list(map(int, input().split())))
    for _ in range(K):
        a, b = map(int, input().split())
        rotate(a, b)
        # for m in magnet: print(m)
    ans = 0
    for i in range(1, 5):
        if magnet[i][0] == 1:
            ans += 2**(i-1)
    print("#{} {}".format(T, ans))