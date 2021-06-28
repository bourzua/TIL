n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList = sorted(numList)

visited = [False]*n
numbers = [0]*m

def go(idx, n, m, start):
    if idx == m:
        print(' '.join(map(str, numbers)))
        return
    for i in range(start,n):
        if visited[i]:
            continue
        visited[i] = True
        numbers[idx] = numList[i]
        go(idx+1, n, m, i+1)
        visited[i] = False

go(0, n, m, 0)