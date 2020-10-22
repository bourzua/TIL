import sys
sys.stdin = open("5102.txt","r")

def BFS(S):
    q = []
    visited[S] = 1
    q.append(S)

    while len(q) > 0:
        s = q.pop(0)
        for i in range(1, V+1):
            if arr[s][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[s] + 1

for T in range(1, int(input())+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a][b] = arr[b][a] = 1
    S, G = map(int, input().split())
    BFS(S)
    ans = 0
    if visited[G] != 0:
        ans = visited[G] - 1

    print("#{} {}".format(T, ans))