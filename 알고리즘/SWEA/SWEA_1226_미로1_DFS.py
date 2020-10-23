import sys
sys.stdin = open("1226.txt","r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def DFS(r,c):
    global key

    visited[r][c] = 1

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]

        if nr<0 or nr>=16 or nc<0 or nc>=16:
            continue
        elif miro[nr][nc] == 1 or visited[nr][nc] != 0:
            continue
        elif miro[nr][nc] == 3:
            key = 1
            return key
        DFS(nr,nc)

for T in range(1, 11):
    N = input()
    miro = [list(map(int, input())) for _ in range(16)]

    visited = [[0]* 16 for _ in range(16)]

    key = 0

    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                DFS(i,j)

    print("#{} {}".format(T, key))