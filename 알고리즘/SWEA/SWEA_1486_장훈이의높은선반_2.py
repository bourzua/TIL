import sys
sys.stdin = open("1486.txt","r")

def powerset(idx):
    global MIN

    if idx == N:
        total = 0
        for i in range(N):
            if sel[i]:
                total += clerk[i]
            if total >= B:
                if total < MIN:
                    MIN = total
        return

    sel[idx] = 1
    powerset(idx+1)

    sel[idx] = 0
    powerset(idx+1)


for T in range(1, int(input())+1):
    N, B = map(int, input().split())
    clerk = list(map(int, input().split()))
    # print(clerk)
    MIN = 9999999999
    sel = [0]*N
    powerset(0)


    print("#{} {}".format(T, MIN-B))