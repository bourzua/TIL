import sys

N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
ans = 0

time.sort(reverse=True)

for i in range(len(time)):
    ans += time[i]*(i+1)

print(ans)