import sys
sys.stdin = open("1873.txt", "r")

tank = ['^', 'v', '<', '>']
dir_dict = {'U':0, 'D':1, 'L':2, 'R':3}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



for T in range(1, int(input())+1):
    H, W = map(int, input().split())
    game = [list(input()) for _ in range(H)]

    N = int(input())
    cmd_list = list(input())

    # 1. 탱크 위치 찾기
    r = c = dir = -1
    for i in range(H):
        for j in range(W):
            if game[i][j] in tank:
                r = i
                c = j
                dir = tank.index(game[i][j])
                break
        if r != -1:
            break
    # 2. 명령어 처리
    for cmd in cmd_list:
        # 2-1. 포탄발사
        if cmd == 'S':
            nr = r + dr[dir]
            nc = c + dc[dir]

            while 0 <= nr < H and 0 <= nc < W:
                if game[nr][nc] == '#': break
                if game[nr][nc] == '*':
                    game[nr][nc] = '.'
                    break
                nr += dr[dir]
                nc += dc[dir]
        # 2-2. 방향조종
        else:
            dir = dir_dict[cmd]
            # 전차방향 바꾸기
            game[r][c] = tank[dir]

            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0<=nr<H and 0<nc<W and game[nr][nc] == '.':
                game[nr][nc] = tank[dir]
                game[r][c] = '.'
                r, c = nr, nc
    # 3. 출력
    print("#{}".format(T), end=" ")
    for i in range(H):
        print("".join(game[i]))