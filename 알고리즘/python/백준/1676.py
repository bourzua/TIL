import sys
N = int(sys.stdin.readline())
fact = 1
count = 0

for i in range(1, N+1):
    fact *= i

for i in range(1, len(str(fact))):
    if fact%(10**i) == 0:
        count += 1
    else:
        break

print(count)