import sys
sys.stdin = open("5189.txt", "r")
# 순열
def perm(n, k):
    global MIN
    # 다 바꾸고 나면 total 체크
    if n == k:
        total = 0
        # 처음과 끝은 항상 1이니까
        total += arr[1][path[0]]
        total += arr[path[-1]][1]

        # 1 사이에서의 경로 계산
        for i in range(len(path)-1):
            total += arr[path[i]][path[i+1]]
        if total < MIN:
            MIN = total
        return

    else:
        for i in range(n, k):
            path[n], path[i] = path[i], path[n]
            perm(n+1, k)
            path[n], path[i] = path[i], path[n]

for T in range(1, int(input())+1):
    N = int(input())
    arr = [[0]*(N+1)]

    for i in range(N):
        arr.append([0] + list(map(int, input().split())))

    # 1 사이의 지점들
    path = [i for i in range(2, N+1)]
    MIN = 0xffffffffff
    perm(0, len(path))

    print("#{} {}".format(T, MIN))