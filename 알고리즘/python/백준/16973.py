    from collections import deque

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def get_sum(r1, c1, r2, c2):
        return s[r2][c2] - s[r1-1][c2] - s[r2][c1-1] + s[r1-1][c1-1]

    n, m = map(int, input().split())
    a = [[0]*(m+1) for _ in range(n+1)]
    s = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        a[i][1:] = list(map(int, input().split()))
    visited = [[-1]*(m+1) for _ in range(n+1)]
    height, width, firstR, firstC, endR, endC = map(int, input().split())

    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j]

    q = deque()
    q.append([firstR, firstC])
    visited[firstR][firstC] = 0

    while q:
        r, c = q.popleft()

        for a in range(4):
            nr = r + dr[a]
            nc = c + dc[a]

            if 1 <= nr and nr+height-1 <= n and 1 <= nc and nc+width-1 <= m:
                if get_sum(nr, nc, nr+height-1, nc+width-1) == 0:
                    if visited[nr][nc] == -1:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append([nr, nc])
    
    print(visited[endR][endC])