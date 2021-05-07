def solution(n, computers):
    answer = 0
    visited = [0] * n

    def BFS(v):
        visited[v] = 1
        q = [v]
        while q:
            curr = q.pop(0)
            for i in range(n):
                if i != curr and computers[curr][i] == 1:
                    if visited[i] == 0:
                        visited[i] = 1
                        q.append(i)

    for i in range(n):
        if visited[i] == 0:
            BFS(i)
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))