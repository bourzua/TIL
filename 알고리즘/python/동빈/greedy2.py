N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

sum = 0
count = 0

for i in range(M):
    if count < K:
        sum += numbers[0]
        count += 1
    else:
        sum += numbers[1]
        count = 0

print(sum)