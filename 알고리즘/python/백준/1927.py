import sys

n = int(sys.stdin.readline())
numList = []

for i in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(numList) == 0:
            print(0)
        else:
            print(min(numList))
            numList.remove(min(numList))
    else:
        numList.append(m)

