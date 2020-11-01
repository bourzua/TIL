import sys
sys.stdin = open("5201.txt", "r")

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    # print(M, N)

    freight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 내림차순으로 정렬
    freight.sort(reverse=True)
    truck.sort(reverse=True)

    i = j = ans = 0

    while i < N and j < M:
        if freight[i] <= truck[j]:
            ans += freight[i]
            i, j = i + 1, j + 1
        else:
            i += 1

    print("#{} {}".format(T, ans))
