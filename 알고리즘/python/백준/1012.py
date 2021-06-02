dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    q = [(r,c)]
    visited[r][c] = 1
    while q:
        curr_r, curr_c = q.pop(0)

        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]

            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if arr[nr][nc] == 0:
                continue
            if visited[nr][nc] != 0:
                continue
            q.append((nr,nc))
            visited[nr][nc] = 1

for T in range(1, int(input())+1):
    M, N, K = map(int, input().split())

    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1

    count = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                BFS(i,j)
                count += 1

    print(count)