from itertools import permutations

N, M = map(int, input().split())
numList = [i for i in range(1, N+1)]
hi = list(permutations(numList, M))
print(hi)