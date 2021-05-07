def solution(n, computers):
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        elif x > y:
            parent[x] = y
            return
        else:
            parent[y] = x
            return

    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j]:
                union(i, j)

    for i in range(n):
        find(i)

    parent = set(parent)
    answer = len(parent)
    return answer