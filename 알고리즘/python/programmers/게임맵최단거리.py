from collections import deque

def solution(maps):
    answer = -1

    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    n, m = len(maps), len(maps[0])
    visited = [[-1] * m for _ in range(n)]

    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    while q:
        r, c = q.popleft()

        for a in range(4):
            nr = r + dr[a]
            nc = c + dc[a]

            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1 and maps[nr][nc] == 1:
                q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1

    answer = visited[-1][-1]
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))