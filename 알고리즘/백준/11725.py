N = int(input())

# 이전에 방문
visited = [0 for _ in range(N+1)]
# 방문한 것은 부모 가능
visited[1] = 1
# 인덱스가 자식, 그 값은 인덱스의 부모
parent = [[] for _ in range(N+1)]


for i in range(N-1):
    a, b = map(int, input().split())
    # 부모랑 자식을 주니까 둘 중 한곳만 들렀을 수밖에 없음
    # 방문한 적이 있을 경우 부모 노드이므로
    # 자식의 자리에 부모 append
    # 자식도 부모가 될 수 있으니까 1
    if visited[a] == 1:
        parent[b] = a
        visited[b] = 1
    elif visited[b] == 1:
        parent[a] = b
        visited[a] = 1

for i in range(2, N+1):
    print(parent[i])