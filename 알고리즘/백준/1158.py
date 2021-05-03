import sys
N, K = map(int, sys.stdin.readline().split())

numbers = list(range(1, N+1))
stack = []
i = 0

while numbers:
    i = (i - 1 + K) % len(numbers)
    stack.append(str(numbers.pop(i)))

print('<' + ', '.join(stack) + '>')