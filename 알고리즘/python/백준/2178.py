dr= [-1, 1, 0, 0]
dc= [0, 0, -1, 1]

def BFS(r, c):
    visited[r][c] = 1
    q = [(r, c)]

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
            visited[nr][nc] = visited[curr_r][curr_c] + 1
            q.append((nr,nc))


N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

BFS(0, 0)

print(visited[N-1][M-1])