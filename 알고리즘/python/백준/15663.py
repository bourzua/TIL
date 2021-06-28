n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList = sorted(numList)
visited = [False]*n

numbers = [0]*m
printList = []

def go(idx, n, m):
    if idx == m:
        tmp = ' '.join(map(str, numbers))
        if tmp not in printList:
            print(tmp)
            printList.append(tmp)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        numbers[idx] = numList[i]
        go(idx+1, n, m)
        visited[i] = False

go(0, n, m)