N, M = map(int, input().split())

rowMin = 0
ans = 0
for i in range(N):
    cards = list(map(int, input().split()))
    rowMin = min(cards)
    ans = max(ans, rowMin)

print(ans)