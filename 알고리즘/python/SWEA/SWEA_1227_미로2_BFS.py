import sys
sys.stdin = open("1227.txt","r")

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r, c):
    global result

    visited[r][c] = 1
    q = [(r,c)]

    while len(q):
        curr_r, curr_c = q.pop(0)

        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]

            if nr<0 or nr>=100 or nc<0 or nc>=100:
                continue
            elif miro[nr][nc] == 1 or visited[nr][nc] != 0:
                continue
            elif miro[nr][nc] == 3:
                result = 1
                return
            visited[nr][nc] = 1
            q.append((nr,nc))

for T in range(1, 11):
    N = input()
    miro = [list(map(int, input())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]
    result = 0

    for i in range(100):
        for j in range(100):
            if miro[i][j] == 2:
                BFS(i, j)

    print("#{} {}".format(T, result))