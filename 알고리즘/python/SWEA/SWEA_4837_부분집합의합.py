import sys
sys.stdin = open("4837.txt","r")

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
M = len(numberList)

def com(idx,sidx):
    global count
    if sidx == N:
        if sum(sel) == K:
            print(sel)
            count +=1
        return
    if idx == M:
        return

    sel[sidx] = numberList[idx]
    # 뽑고가고
    com(idx + 1, sidx + 1)
    # 안뽑고가고
    com(idx + 1, sidx)

# for T in range(1, int(input())+1):
T = int(input())
for T in range(1, T+1):


    N, K = map(int, input().split())

    sel = [0]*N
    count = 0

    com(0,0)



    print("#{} {}".format(T, count))