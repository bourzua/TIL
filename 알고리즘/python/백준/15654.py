n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList = sorted(numList)
visited = [False]*n

numbers = [0]*m

def go(idx, n, m):
    if idx == m:
        print(' '.join(map(str, numbers)))
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        numbers[idx] = numList[i]
        go(idx+1, n, m)
        visited[i] = False

go(0, n, m)