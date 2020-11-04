di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def BFS(arr1):
    q = []
    for i in range(N):
        for j in range(M):
            if arr1[i][j] == 2:
                q.append((i, j))
    while q:
        curr_r, curr_c = q.pop(0)

        for a in range(4):

            nr = curr_r + di[a]
            nc = curr_c + dj[a]

            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if arr1[nr][nc] == 1 or arr1[nr][nc] == 2:
                continue
            arr1[nr][nc] = 2
            q.append((nr, nc))
    count = 0
    for i in range(N):
        for j in range(M):
            if arr1[i][j] == 0:
                count += 1
    return count


def virus(rest):
    global MAX
    if rest == 0:
        if BFS(lab) > MAX:
            MAX = BFS(lab)
        return

    for i in range(N):
        for j in range(M):
            # 방문했던 건 건너뛰기
            if visited[i][j]:
                continue
            if lab[i][j] == 0:
                lab[i][j] = 1
                visited[i][j] = 1
                virus(rest - 1)
                lab[i][j] = 0
                visited[i][j] = 0
                virus(rest)



N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

MAX = 0

virus(3)

print(MAX)