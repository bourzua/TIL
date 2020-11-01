# visited 필요없다
# 델타이동 꼭 필요한 게 X

def dfs(i, j, style):
    global count
    if i == N and j == N:
        count += 1
        return

    if style == 1:
        if j == N:
            return
        if pipe[i][j+1] == 0:
            dfs(i, j+1, 1)
            if pipe[i+1][j+1] == 0 and pipe[i+1][j] == 0:
                dfs(i+1, j+1, 3)
            return

    elif style == 2:
        if i == N:
            return
        if pipe[i+1][j] == 0:
            dfs(i+1, j, 2)
            if pipe[i+1][j+1] == 0 and pipe[i][j+1] == 0:
                dfs(i+1, j+1, 3)
            return

    elif style == 3:
        if j == N:
            for a in range(i, N):
                if pipe[a][j] == 1:
                    return
            count += 1
            return

        elif i == N:
            for a in range(j, N):
                if pipe[i][a] == 1:
                    return
            count += 1
            return

        if pipe[i+1][j+1] == 0 and pipe[i+1][j] == 0 and pipe[i][j+1] == 0:
            dfs(i+1, j, 2)
            dfs(i+1, j+1, 3)
            dfs(i, j+1, 1)
            return

        if pipe[i+1][j] == 0:
            dfs(i+1, j, 2)

        if pipe[i][j+1] == 0:
            dfs(i, j+1, 1)

        if pipe[i][j+1] == 0:
            dfs(i, j+1, 1)
        if pipe[i+1][j] == 0:
            dfs(i+1, j, 2)
        if pipe[i+1][j+1] == 0 and pipe[i+1][j] == 0 and pipe[i][j+1] == 0:
            dfs(i+1, j+1, 3)



N = int(input())

pipe = [[0]*(N+1)]

for i in range(N):
    pipe.append([0] + list(map(int, input().split())))

count = 0

dfs(1, 2, 1)

print(count)