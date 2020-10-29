# DFS로 풀었는데 실패
# 최단거리를 찾는거니까 BFS

def BFS(v):
    global count

    a = [v]

    while q:
        if


    for i in range(1, N+1):
        if family[v][i] == 1 and visited[i] == 0:
            count +=1
            DFS(i)


# N = int(input())
N = 9

# a, b = map(int, input().split())
a, b = 7, 3
# M = int(input())
M = 7

family = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

family = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]

# for i in range(M):
#     a, b = map(int, input().split())
#     family[a][b] = family[b][a] = 1
count = 0
BFS(a)
print(count)
