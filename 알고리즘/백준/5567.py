N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0]*(N+1)
visited[1] = 1
friends = []
for i in arr[1]:
    friends.append(i)
    visited[i] = 1
count = 0
for friend in friends:
    for i in arr[friend]:
        if visited[i] == 0:
            count += 1
            # 방문체크 잊지말기
            visited[i] = 1
print(len(friends)+count)