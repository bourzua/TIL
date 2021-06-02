# 순서 고려 => permutations

from itertools import permutations
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

cards = [sys.stdin.readline().rstrip() for _ in range(N)]

result = set()

for i in permutations(cards, K):
    result.add(''.join(i))

print(len(result))