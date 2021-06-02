import sys
sys.stdin = open("1247.txt", "r")

def DFS(start, dist):
    global MIN
    if dist > MIN:
        return
    if visited.count(1) == N+2:
        dist += abs(xyList[start][0] - xyList[1][0]) + abs(xyList[start][1] - xyList[1][1])
        if dist < MIN:
            MIN = dist
        return

    for i in range(2, N+2):
        if visited[i] == 0:
            newdist = abs(xyList[start][0] - xyList[i][0]) + abs(xyList[start][1]-xyList[i][1])
            visited[i] = 1
            DFS(i, dist+newdist)
            visited[i] = 0

for T in range(1, int(input())+1):
    N = int(input())

    numList = list(map(int, input().split()))
    xyList = []

    for i in range(0, N+2):
        xyList.append((numList[2*i], numList[2*i + 1]))

    visited = [0 for _ in range(N+2)]
    visited[0] = visited[1] = 1
    MIN = 0xfffffff
    DFS(0, 0)

    print("#{} {}".format(T, MIN))