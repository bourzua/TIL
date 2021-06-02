def rotate(arr):
    global rec
    new = [[0]*M for _ in range(N)]
    for i in range(rotateNumber):
        for a in range(i, N-i):
            for b in range(i, M-i):
                if a == i and i<b<M-i:
                    new[a][b-1] = arr[a][b]
                elif b == M-i-1 and i<a<N-i:
                    new[a-1][b] = arr[a][b]
                elif a == N-i-1 and i<=b<M-i-1:
                    new[a][b+1] = arr[a][b]
                elif b == i and i<=a<N-i-1:
                    new[a+1][b] = arr[a][b]
    rec = new


N, M, R = map(int, input().split())
rotateNumber = min(N,M) // 2

rec = []

for i in range(N):
    rec.append(list(map(int, input().split())))

for i in range(R):
    rotate(rec)

for i in range(N):
    for j in range(M):
        print(rec[i][j], end=" ")
    print()