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

    total = 0
    for i in range(M):
        for j in range(N):
            # 트럭에 화물 담을 수 있으면
            if truck[i] >= freight[j]:
                # total에 화물 무게 추가
                total += freight[j]
                # 골라진 것 이전은 트럭에 담을 수 없게
                for a in range(j+1):
                    freight[a] = 51
                break
    print("#{} {}".format(T, total))
