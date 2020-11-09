import sys
sys.stdin = open("5247.txt","r")

from collections import deque

for T in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    k = 0
    q = deque()
    q.append((N, 0))
    records = set()
    while True:
        num, cnt = q.popleft()
        if num == M: k = cnt; break
        if num * 2 not in records and 1 <= num <= 1000000: q.append((num * 2, cnt + 1)); records.add(num * 2)
        if num + 1 not in records and 1 <= num <= 1000000: q.append((num + 1, cnt + 1)); records.add(num + 1)
        if num - 1 not in records and 1 <= num <= 1000000: q.append((num - 1, cnt + 1)); records.add(num - 1)
        if num - 10 not in records and 1 <= num <= 1000000: q.append((num - 10, cnt + 1)); records.add(num - 10)
    print('#{} {}'.format(T, k))