from _collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS():
    q = deque()
    q.append([0, 0, 1])
    visited = [[[0,0] for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1

    while q:
        a, b, x = q.popleft()


        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]

            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if punch[nr][nc] == 1:
                continue
            if visited[nr][nc] != 0:
                continue
            visited[nr][nc] = visited[curr_r][curr_c] + 1
            q.append((nr,nc))



N, M = map(int, input().split())

punch = [list(map(int, input())) for _ in range(N)]

print(BFS())
