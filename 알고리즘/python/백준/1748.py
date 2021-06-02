import sys
N = int(sys.stdin.readline())

ans = 0

last = len(str(N))

for i in range(1, last):
    ans += (10**(i-1))*9*i

lastSum = (N - 10**(last-1) + 1)*last
ans += lastSum

print(ans)