import sys
sys.stdin = open("1267.txt","r")

def DFS(v):
    global result
    visited[v] = 1
    # 수행하면 추가
    result += str(v) + " "

    # 수행 후 해당 노드를 선행 노드로 둔 노드의 선행노드수 -1
    for i in range(1, V+1):
        if arr[v][i]:
            burdenList[i] -= 1

    # 수행한 노드에서 갈수있는 곳 & 수행하지 X & 선행노드수 0
    # 일 경우에 넘어갈 수 있음
    for i in range(1, V + 1):
        if arr[v][i] == 1 and visited[i]==0 and burdenList[i] == 0:
            DFS(i)



for T in range(1, 11):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]

    # 일을 수행했는지 여부
    visited = [0]*(V+1)

    path = list(map(int, input().split()))

    for i in range(0, len(path),2):
        arr[path[i]][path[i+1]] = 1

    # 노드별로 선행노드가 몇갠지
    # 선행노드가 0개: 해당 노드 수행가능
    burdenList = [0]*(V+1)

    startList = []

    # 시작노드 구하기
    # 다른 노드에서 오는 간선이 없는 노드에서 시작가능
    for i in range(1, V+1):
        count = 0
        for j in range(1, V+1):
            count += arr[j][i]
        if count == 0:
            startList.append(i)

    # 노드별 선행노드 개수
    for i in range(1, V+1):
        burden = 0
        for j in range(1,V+1):
            burden += arr[j][i]
        burdenList[i] = burden

    # 시작점마다 DFS수행
    result = ''
    for i in startList:
        DFS(i)

    print("#{} {}".format(T, result))