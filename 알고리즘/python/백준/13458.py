N = int(input())
candidates = list(map(int, input().split()))
B, C = map(int, input().split())
total = N
for i in range(N):
    if candidates[i] < B:
        continue
    else:
        plus = (candidates[i] - B) // C
        if (candidates[i] - B) % C:
            plus += 1
        total += plus
print(total)