# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r,c):
    queue = [(r,c)]
    dist[r][c] = 1

    while len(queue)>0 :
        curr_r, curr_c = queue.pop(0)

        #4방향 탐색
        for i in range(4):
            nr = curr_r+dr[i]
            nc = curr_c+dc[i]

            #범위를 벗어났다면 넘어가기
            if nr <0 or nr>= N or nc<0 or nc>=N:
                continue
            #갈수있는자리가 아니거나 이미 거리를 구했다면 넘어가기
            if arr[nr][nc] == 0 or dist[nr][nc] != 0:
                continue

            #그게 아니다.! 거리 갱신 후 큐에 삽입
            queue.append((nr,nc))
            dist[nr][nc] = dist[curr_r][curr_c]+1


N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
#거리를 담을 배열
dist = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and dist[i][j] == 0:
            BFS(i,j)


for i in dist:
    print(*i)