# 문제만 이해하면 창용마을무리의개수와 같은 문제
# 유향그래프
# BFS가 시간 덜 걸림

# def DFS(v):
#     visited[v] = 1
#     for i in range(1, N+1):
#         if graph[v][i] == 1 and visited[i] == 0:
#             DFS(i)

def BFS(v):
    visited[v] = 1
    q = [v]
    while q:
        curr = q.pop(0)
        for i in range(1, N+1):
            if graph[curr][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)

for T in range(1, int(input())+1):
    N = int(input())
    numList = [0] + list(map(int, input().split()))

    graph = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        graph[i][numList[i]] = 1

    visited = [0]*(N+1)
    count = 0

    for i in range(1, N+1):
        if visited[i] == 0:
            # DFS(i)
            BFS(i)
            count += 1

    print(count)