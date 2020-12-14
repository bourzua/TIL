import sys
sys.stdin = open("4871.txt","r")

from collections import deque

def BFS(v):
    global ans
    q = deque()
    q.append(v)

    while q:
        curr_v = q.popleft()
        visited[curr_v] = 1

        for i in range(1, V+1):
            if visited[i] == 0 and game[curr_v][i] == 1:
                if i == G:
                    ans = 1
                    return
                else:
                    q.append(i)



for T in range(1, int(input())+1):
    V, E = map(int, input().split())
    game = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    ans = 0
    for _ in range(E):
        a, b = map(int, input().split())
        game[a][b] = 1
    S, G = map(int, input().split())
    BFS(S)

    print("#{} {}".format(T, ans))