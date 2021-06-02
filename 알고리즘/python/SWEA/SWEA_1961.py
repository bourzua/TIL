import sys
sys.stdin = open("1961.txt","r")

# 오른쪽으로 90도 회전 함수
def rotate(rec):
    newrec = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            newrec[j][N-1-i] = rec[i][j]
    return newrec

for T in range(1, int(input())+1):
    N = int(input())
    rec = []
    for i in range(N):
        rec.append(list(map(int, input().split())))

    rec1 = rotate(rec)
    rec2 = rotate(rec1)
    rec3 = rotate(rec2)

    recSet =[[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            recSet[i].append(rec1[i][j])
        for j in range(N):
            recSet[i].append(rec2[i][j])
        for j in range(N):
            recSet[i].append(rec3[i][j])

    print("#{}".format(T))

    for i in range(N):
        for j in range(N*3):
            if j%N != N-1:
                print(recSet[i][j], end="")
            else:
                print(recSet[i][j], end=" ")
        print()