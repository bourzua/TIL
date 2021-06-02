import sys
sys.stdin = open("1865.txt", "r")

def check(a, p):
    global maxP
    # 어떤 확률을 곱하든 지금보다 더 작아지니까 한번 작게 나오면 끝
    if p <= maxP:
        return
    # 마지막 사람의 성공확률까지 구하면
    if a == N:
        if p > maxP:
            maxP = p
        return
    # 일 정해주기
    for b in range(N):
        # 그 일 안했으면
        if not idx[b]:
            # 체크해주고 확률 곱해주고 다음 자리부터
            idx[b] = 1
            check(a+1, p*success[a][b]*0.01)
            # 원래대로 돌려주기
            idx[b] = 0

for T in range(1, int(input())+1):
    N = int(input())

    success = [list(map(int, input().split())) for _ in range(N)]

    # 일 했는지 안했는지
    idx = [0]*N
    maxP = 0
    check(0, 1)

    print('#{} {:6f}'.format(T, maxP * 100))

