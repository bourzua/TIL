def DFS(start):
    global result
    visited[start] = 1
    for i in range(1, V+1):
        if arr[start][i] == 1 and visited[i] == 0:
            if i == end:
                result = 1
                return result
            DFS(i)



for T in range(1, int(input().split())+1):
    V, E = map(int, input().split())

    arr = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        st, ed = map(int, input().split())
        arr[st][ed] = 1

    visited = [0]*(V+1)

    start, end = map(int, input().split())

    result = 0
    DFS(start)