import sys
sys.stdin = open("5105.txt","r")

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r,c):
    global ans
    q = [(r,c)]

    while len(q)>0:
        curr_r, curr_c = q.pop(0)

        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]

            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            elif miro[nr][nc] == 1 or dist[nr][nc] != 0:
                continue
            elif miro[nr][nc] == 3:
                ans = dist[curr_r][curr_c]
                return
            dist[nr][nc] = dist[curr_r][curr_c] + 1
            q.append((nr,nc))

for T in range(1, int(input())+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    dist = [[0]*N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                BFS(i,j)
                break

    print("#{} {}".format(T, ans))