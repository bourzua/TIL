N = int(input())

for _ in range(N):
    C = int(input())
    com = dict()
    for _ in range(C):
        a, b = input().split()
        if b in com:
            com[b] += 1
        else:
            com[b] = 1
    ans = 1
    for key in com:
        ans *= com[key] + 1

    print(ans - 1)