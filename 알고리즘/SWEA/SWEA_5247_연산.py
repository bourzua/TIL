import sys
sys.stdin = open("5247.txt","r")

from _collections import deque

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    record = set()
    q = deque()
    q.append(N)
    k = 0
    flag = False
    # while M not in q:
    while True:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == M:
                flag = True
                break
            if curr+1 not in record:
                q.append(curr+1)
                record.add(curr+1)
            if curr-1 not in record:
                q.append(curr-1)
                record.add(curr-1)
            if curr*2 not in record:
                q.append(curr*2)
                record.add(curr * 2)
            if curr-10 not in record:
                q.append(curr-10)
                record.add(curr-10)
        if flag == True:
            break
        else:
            k += 1
    print("#{} {}".format(T, k))
