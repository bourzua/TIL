import sys
sys.stdin = open("10888.txt", "r")

for T in range(1, int(input())+1):
    N = int(input())
    MAP = []
    for i in range(N):
        arr = list(map(int, input().split()))
        MAP.append(arr)

    deliveries = []
    client = []

    for i in range(N):
        for j in range(N):
            if MAP[i][j] >=2:
                deliveries.append([i, j, MAP[i][j]])
            elif MAP[i][j] == 1:
                client.append([i, j])

            