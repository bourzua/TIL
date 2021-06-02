M, N = map(int, input().split())

# 에라토스테네스의 체
a = [False, False] + [True]*(N-1)
primes = []

for i in range(2, N+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

for i in primes:
    if M <= i <= N:
        print(i)