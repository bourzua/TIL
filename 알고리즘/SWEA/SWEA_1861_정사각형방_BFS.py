import sys
sys.stdin = open("1861.txt","r")

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r,c):
    global count

    # 큐에 시작점 삽입
    q = [(r,c)]

    while len(q)>0:
        # 큐 맨앞 가져와
        curr_r, curr_c = q.pop(0)

        # 4방향탐색하면서 배열범위 안 & 1만큼큰방 찾기
        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]

            # 자꾸 curr-r, curr_c를 r,c로 써서 허송세월 보냄ㅡㅡ
            if 0<=nr<N and 0<=nc<N and rec[nr][nc]-rec[curr_r][curr_c]==1:
                # 찾았으면 어차피 그방갈거니까 count +1
                count +=1
                # 큐에 새로운방 삽입
                q.append((nr,nc))


for T in range(1, int(input())+1):
    N = int(input())

    rec = [list(map(int, input().split())) for _ in range(N)]

    # 좌표별 count 담을 이차배열 준비
    countArr = [[0]*N for _ in range(N)]

    # 좌표별 count
    for i in range(N):
        for j in range(N):
            count = 1
            BFS(i,j)
            countArr[i][j] = count

    MAX = 0
    for i in range(N):
        for j in range(N):
            if countArr[i][j] > MAX:
                MAX = countArr[i][j]

    minList = []
    for i in range(N):
        for j in range(N):
            if countArr[i][j] == MAX:
                minList.append(rec[i][j])

    print("#{} {} {}".format(T, min(minList), MAX))