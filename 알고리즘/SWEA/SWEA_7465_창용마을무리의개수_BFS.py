import sys
sys.stdin = open("7465.txt","r")

def BFS(v):
    visited[v] = 1
    q = [v]
    while q:
        new = q.pop(0)
        for i in range(1, N+1):
            if arr[new][i]==1 and visited[i]==0:
                q.append(i)
                visited[i] = 1



for T in range(1, int(input())+1):
    N, M = map(int, input().split())

    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = arr[b][a] = 1

    count = 0

    for i in range(1, N+1):
        if visited[i]==0:
            BFS(i)
            count +=1
    print("#{} {}".format(T, count))