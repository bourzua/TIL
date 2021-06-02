# find 연산
def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

# union 연산
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


parent = [0]*6
for i in range(len(parent)):
    parent[i] = i



