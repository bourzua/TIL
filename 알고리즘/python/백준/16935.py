def op1(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = a[n-i-1][j]
    return ans

def op2(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = a[i][m-j-1]
    return ans

def op3(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = a[n-j-1][i]
    return ans

def op4(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = a[j][m-i-1]
    return ans

def op5(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i][j + m//2] = a[i][j]
            ans[i + n//2][j + m//2] = a[i][j + m//2]
            ans[i + n//2][j] = a[i + n//2][j + m//2]
            ans[i][j] = a[i + n//2][j]
    return ans

def op6(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i + n//2][j] = a[i][j]
            ans[i + n//2][j + m//2] = a[i + n//2][j]
            ans[i][j + m//2] = a[i + n//2][j + m//2]
            ans[i][j] = a[i][j + m//2]
    return ans

N, M, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
func = [op1, op2, op3, op4, op5, op6]
for i in list(map(int, input().split())):
    a = func[i-1](a)
for row in a:
    print(*row, sep=' ')