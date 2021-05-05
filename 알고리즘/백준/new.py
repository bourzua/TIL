def BFS(n, v, computers, visited):
    visited[v] = 1
    q = [v]
    while q:
        curr = q.pop(0)
        for i in range(n):
            for j in range(n):
                if computers[i][j] == 1 and i != j:
                    if visited[j] == 0:
                        visited[j] = 1
                        q.append(j)


def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(n):
        if visited[i] == 0:
            BFS(n, i, computers, visited)
            answer += 1
    return answer