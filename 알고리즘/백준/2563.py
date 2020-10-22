colorpaper = [[0]*100 for _ in range(100)]

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    for I in range(10):
        for J in range(10):
            colorpaper[a+I][b+J] = 1

count = 0
for i in range(100):
    for j in range(100):
        if colorpaper[i][j] == 1:
            count +=1

print(count)