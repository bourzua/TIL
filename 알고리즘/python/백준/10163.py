arr = [[0]*101 for _ in range(101)]

N = int(input())
for A in range(1, N+1):
    b, a, width, height = map(int, input().split())

    for i in range(height):
        for j in range(width):
            arr[a+i][b+j] = A

for B in range(1, N+1):
    count = 0
    for i in range(101):
        for j in range(101):
            if arr[i][j] == B:
                count += 1
    print(count)