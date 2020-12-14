import sys
sys.stdin = open("2806.txt", "r")

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def DFS(r, c):
    chess[r][c] = 1





for T in range(1, int(input())+1):
    N = int(input())

    chess = [[0]*N for _ in range(N)]
    cnt = 0
    DFS(0, 0)