import sys
sys.stdin = open("5105.txt","r")

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r,c):
    global key

    queue = [(r,c)]

    while len(queue)>0:
        curr_r, curr_c = queue.pop(0)

        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]

            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            # 여기에서 miro[nr][nc] != 0 했다가 계속 틀렸는데
            # 그렇게 하면 3일 때도 걸리니까 == 1로 물어봤어야함
            if miro[nr][nc] == 1 or dist[nr][nc]!=0:
                continue
            if miro[nr][nc] == 3:
                key = 1
                return dist[curr_r][curr_c]

            queue.append((nr,nc))
            dist[nr][nc] = dist[curr_r][curr_c] + 1


for T in range(1, int(input())+1):
    N = int(input())
    key = 0

    miro = [list(map(int,input())) for _ in range(N)]
    dist = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                number = BFS(i,j)

    if key == 0:
        print("#{} {}".format(T, key))
    else:
        print("#{} {}".format(T, number))