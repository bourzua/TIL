import sys
sys.stdin = open("5249.txt", "r")

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union_set(x, y):
    p[find_set(y)] = find_set(x)

for T in range(1, int(input())+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    p = [0]*(V+1)
    edges = sorted(edges, key=lambda x:x[2])
    for i in range(V+1):
        make_set(i)
    ans = 0
    # 간선수 0부터 시작했으니까 V개 뽑기
    cnt = 0
    idx = 0
    while cnt < V:
        x = p[edges[idx][0]]
        y = p[edges[idx][1]]
        if find_set(x) != find_set(y):
            union_set(x, y)
            cnt += 1
            ans += edges[idx][2]
        # 뽑든 안뽑든 다음 항목으로 넘어가야 하니까
        idx += 1
    print("#{} {}".format(T, ans))