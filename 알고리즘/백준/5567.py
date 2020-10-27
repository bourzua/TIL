N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
# 상근이로 시작
visited[1] = 1
M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1


friends = []
for i in range(2, N+1):
    if arr[1][i] == 1:
        visited[i] = 1
        friends.append(i)
firstFriends = len(friends)

for i in friends:
    for j in range(2, N+1):
        if arr[i][j] == 1 and visited[j] == 0:
            # 친구들의 친구가 같을 수 있으니까
            visited[j] = 1
            firstFriends += 1

print(firstFriends)
