N = int(input())

line = []

number = list(map(int, input().split()))

for i in range(N):
    a = len(line) - number[i]
    line.insert(a, i+1)

for i in range(len(line)):
    print(line[i], end=" ")