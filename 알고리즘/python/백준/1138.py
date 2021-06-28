n = int(input())
ans = [0]*n
left = list(map(int, input().split()))

for i in range(n):
    number = left[i]
    count = 0
    for j in range(n):
        if number == count and ans[j] == 0:
            ans[j] = i + 1
            break
        if ans[j] == 0:
            count += 1

print(*ans)