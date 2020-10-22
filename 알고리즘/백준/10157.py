# 격자를 시계방향으로 90도 회전시켜서 생각해보면 행렬로 생각할 수 있음
row, column = map(int, input().split())
K = int(input())

# 시간을 줄이기 위해 초장부터 잡아주기
if K > row*column:
    print(0)
else:
    # 계산하기 어려우니 0행과 0열 추가
    chair = [[0]*(column+1) for _ in range(row+1)]

    # 0행과 0열은 가면 안되니까 갈 수 있는 좌표 값 1로 주기
    for i in range(1, row+1):
        for j in range(1, column+1):
            chair[i][j] = 1


    # 방향: 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # idx
    dir = 0

    # 시작점
    r=1
    c=0
    num=0

    # K 전에 끝나니까
    while num < K:
        num += 1

        nr = r + dr[dir]
        nc = c + dc[dir]

        # 범위 안넘고, 방문 안했던 곳
        if 0<nr<=row and 0<nc<=column and chair[nr][nc] == 1:
            r, c = nr, nc
        else:
            # 방향 변경
            dir = (dir+1)%4
            r += dr[dir]
            c += dc[dir]
        # 방문했던 곳은 2로 설정
        chair[r][c] = 2

    print(r, c)