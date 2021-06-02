N, K = map(int, input().split())

sumList = []

temp = list(map(int, input().split()))

for i in range(N-K+1):
    sum = 0
    for j in range(K):
        sum += temp[i+j]
    sumList.append(sum)

print(max(sumList))