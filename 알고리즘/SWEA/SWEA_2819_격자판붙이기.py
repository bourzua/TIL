import sys
sys.stdin = open("2819.txt","r")

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def DFS(r,c,path):
    global s1
    # 종료조건을 어디에 줘야하는지 너무 헷갈림
    if len(path) == 7:
        s1.add(path)
        return

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if nr<0 or nr>=4 or nc<0 or nc>=4:
            continue
        DFS(nr,nc,path + arr[nr][nc])

for T in range(1, int(input())+1):

    arr = [input().split() for _ in range(4)]

    s1 = set()

    for i in range(4):
        for j in range(4):
            DFS(i,j,arr[i][j])

    print("#{} {}".format(T,len(s1)))