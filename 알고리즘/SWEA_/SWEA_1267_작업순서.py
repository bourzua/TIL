import sys
sys.stdin = open("1267.txt","r")

def BFS(v):
    global result
    visited[v] = 1
    for i in range(1, V+1):
        if arr[v][i]:
            burdenList[i] -= 1
    q = [v]

    while len(q)>0:

        new = q.pop(0)

        result += str(new) + " "


        for i in range(1, V+1):
            if arr[new][i]==1 and visited[i] == 0 and burdenList[i] == 0:
                q.append(i)


for T in range(1, 11):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)

    path = list(map(int, input().split()))

    for i in range(0, len(path),2):
        arr[path[i]][path[i+1]] = 1

    burdenList = [0]*(V+1)
    startList = []
    for i in range(1, V+1):
        count = 0
        for j in range(1, V+1):
            count += arr[j][i]
        if count == 0:
            startList.append(i)

    for i in range(1, V+1):
        burden = 0
        for j in range(1,V+1):
            burden += arr[j][i]
        burdenList[i] = burden

    result = ''
    for i in startList:
        BFS(i)
    # resultList = list(map(int, result.split()))
    #
    # for i in range(1, V+1):
    #     if i not in resultList:
    #         result += str(i)

    print("#{} {}".format(T, result))