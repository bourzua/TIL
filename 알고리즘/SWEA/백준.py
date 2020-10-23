def BFS(v):
    queue = [v]
    visited[v] = 1

    while queue:
        curr = queue.pop(0)

        for i in adj[curr]:
            if not visited[i]:
                visited[i]
                queue.append(i)

for T in range(1, int(input())+1):
    V, E = map(int, input().split())

    # 인접리스트
    adj = [[] for _ in range(V+1)]

    for i in range(E):
        A, B = map(int, input().split())
        adj[A].append(B)
        adj[B].append(A)

    visited = [0]*(V+1)

    ans = 0
    for i in range(1, V+1):
        if visited[i] == 0:
            ans += 1
            BFS(i)

    print("#{} {}".format(T,ans))