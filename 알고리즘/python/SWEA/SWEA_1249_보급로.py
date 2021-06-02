import sys
sys.stdin = open("1249.txt", "r")

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(i, j):
    q = deque()
    q.append((i, j))
    while q:
        curr_i, curr_j = q.popleft()
        if curr_i == curr_j == N-1:
            continue
        for a in range(4):
            ni = curr_i + di[a]
            nj = curr_j + dj[a]
            if ni<0 or ni>=N or nj<0 or nj>=N:
                continue
            if ni == 0 and nj == 0:
                continue
            # 맨처음 가는 것이 최소가 될 수 있음 / 그 다음부터는 더 작은값 넣어주기
            if record[ni][nj] == -1 or record[curr_i][curr_j] + arr[ni][nj] < record[ni][nj]:
                record[ni][nj] = record[curr_i][curr_j] + arr[ni][nj]
                q.append((ni, nj))

#1 2
#2 2
#3 8
#4 57
#5 151
#6 257
#7 18
#8 160
#9 414
#10 395
for T in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    record = [[-1]*N for _ in range(N)]
    # 이것이 키포인트
    record[0][0] = arr[0][0]
    BFS(0,0)
    print("#{} {}".format(T, record[N-1][N-1]))