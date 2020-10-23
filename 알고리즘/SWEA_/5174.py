import sys
sys.stdin = open("5174.txt", "r")

for T in range(1, int(input())+1):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E+2)]
    a = list(map(int, input().split()))
    for i in range(E):
        x, y = a[i*2], a[i*2+1]
        tree[x].append(y)
    # print(tree)

    q = [N]
    count = 1

    while q:
        v = q.pop(0)

        for i in tree[v]:
            q.append(i)
            count +=1
    print("#{} {}".format(T, count))
