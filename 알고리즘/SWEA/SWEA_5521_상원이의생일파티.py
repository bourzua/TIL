import sys
sys.stdin = open("5521.txt","r")


for T in range(1, int(input())+1):
    N, M = map(int, input().split())

    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = arr[b][a] = 1

    friends = []
    for i in range(2, N+1):
        if arr[1][i] == 1:
            friends.append(i)
            visited[i] = 1
    count = 0
    for friend in friends:
        for j in range(2, N+1):
            if arr[friend][j] == 1 and visited[j] == 0:
                count += 1
                visited[j] = 1

    ans = len(friends) + count
    print("#{} {}".format(T, ans))