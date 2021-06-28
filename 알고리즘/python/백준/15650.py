n,m = map(int,input().split())
visited = [False] * (n + 1)
a = [0]*m

def go(index, n, m, start):
    if index == m:
        print(' '.join(map(str,a)))
        return
    for i in range(start, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        a[index] = i
        go(index+1, n, m, i+1)
        visited[i] = False

go(0, n, m, 1)