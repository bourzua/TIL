import sys
N, M = map(int, sys.stdin.readline().split())
ear = set(sys.stdin.readline().rstrip() for _ in range(N))

two = []
for _ in range(M):
    temp = sys.stdin.readline().rstrip()
    if temp in ear:
        two.append(temp)

print(len(two))
for i in sorted(two):
    print(i)