dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def check(r, c):
    count = 0
    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if ice[nr][nc] == 0:
            count += 1

    return count
# def ice_count():
#     count = 0
#     visited = [[0]*N for _ in range(M)]
#     for i in range(N):
#         for j in range(M):
#             if visited[i][j] == 0 and ice[i][j] != 0:
#                 count += 1



N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
minus = [[0]*M for _ in range(N)]
count = 0

while True:
