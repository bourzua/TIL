import sys
sys.stdin = open("1486.txt","r")


def combination(idx, sidx, R):
    global sumSet

    # 조합 원소들의 합이 B보다 같거나 크면 Sumset에 add
    # set이니까 겹쳐도 상관없음
    if sidx == R:
        if sum(sel) >= B:
            sumSet.add(sum(sel))
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combination(i + 1, sidx + 1, R)

for T in range(1, int(input())+1):
    N, B= map(int, input().split())
    arr = list(map(int, input().split()))

    sumSet = set()
4
    # 원소수별로 조합 다 만드는 함수 이용
    for i in range(1, N+1):
        # i개만큼 칸 만들어줌
        sel = [0]*i
        combination(0, 0, i)

    print("#{} {}".format(T, min(sumSet)-B))