# 전체 - 팀을 이룰 수 있는것 이렇게 구하자

def DFS(v):
    global passed
    global dfsPath

    # 만약에 v가 dfsPath에 있으면 그 위치부터 반복됨
    if v in dfsPath:
        # 팀에 못끼는 애나 팀된애들이나 이제 접근하면 안되므로 방문처리
        for i in dfsPath:
            visited[i] = 1
        # 반복의 시작부터 끝까지 개수 세주기
        # 반복 아닌 부분은 세면 안되니까
        for i in range(len(dfsPath)):
            if dfsPath[i] == v:
                for j in range(i, len(dfsPath)):
                    passed += 1
        # for i in range(p,len(dfsPath)):
        #     passed += 1
        return
    # 일단 넣어주고
    dfsPath.append(v)

    # 다음놈이 접근가능하면 DFS돌리기
    if visited[team[v]] == 0:
        DFS(team[v])

for T in range(1, int(input())+1):
# for T in range(1, 2):
    N = int(input())
    team = [0] + list(map(int, input().split()))
    visited = [0]*(N+1)

    # 팀플가능한애들 수
    passed = 0
    # 혼자 노는 애있으면 팀플가능수에 넣고 접근못하게 하자
    for i in range(1, N+1):
        if team[i] == i:
            visited[i] = 1
            passed += 1
    # for i in range(1, N+1):


    for i in range(1, N+1):
        dfsPath = []
        if visited[i] == 0:
            DFS(i)

    print(N-passed)