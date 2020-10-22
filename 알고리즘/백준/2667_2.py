dr = [-1,1,0,0]
dc = [0,0,-1,1]

def DFS(r,c):
    global BFS_count
    visited[r][c] = 1
    BFS_count += 1

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]

        if nr<0 or nr>=N or nc<0 or nc>=N:
            continue
        if arr[nr][nc] == 1 and visited[nr][nc] == 0:
            DFS(nr, nc)

N = int(input())
arr = []
visited = [[0]*(N) for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, input())))

count = 0
BFS_count_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            BFS_count = 0
            DFS(i, j)
            count += 1
            BFS_count_list.append(BFS_count)

BFS_count_list.sort()

print(count)
for i in range(count):
    print(BFS_count_list[i])