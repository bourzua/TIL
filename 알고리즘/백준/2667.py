dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r,c):
    global BFS_count
    q = [(r,c)]
    visited[r][c] = 1
    while q:
        BFS_count += 1
        curr_r, curr_c = q.pop(0)

        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]
            if nr>=N or nr<0 or nc>=N or nc<0:
                continue
            # if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                # visited[nr][nc] = 1
                # q.append((nr,nc))
            if arr[nr][nc] == 0:
                continue
            if visited[nr][nc] != 0:
                continue
            visited[nr][nc] = visited[curr_r][curr_c] + 1
            q.append((nr,nc))

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
            BFS(i, j)
            count += 1
            BFS_count_list.append(BFS_count)

BFS_count_list.sort()

print(count)
for i in range(count):
    print(BFS_count_list[i])