def rotate(idx, d):
    if d==1:
        magnet[idx].insert(0, magnet[idx].pop())
    else:
        magnet[idx].append(magnet[idx].pop(0))

def func(idx, d):
    check[idx] = 1

    # 오른쪽 자석을 돌릴 수 있다면
    if idx < 4 and magnet[idx][2] != magnet[idx+1][6] and not check[idx+1]:
        func(idx+1, -d)

    # 왼쪽 자석을 돌릴 수 있다면
    if idx > 1 and magnet[idx][6] != magnet[idx-1][2] and not check[idx-1]:
        func(idx-1, -d)

    rotate(idx, d)

for T in range(1, int(input())+1):
    K = int(input())
    ans = 0

    magnet = [[0]] + [list(map(int, input().split())) for _ in range(4)]

    for i in range(K):
        # 몇번자석을 어디방향으로?
        idx, d = map(int, input().split())

        # 자석이 돌았는지 체크하는 리스트
        check = [0]*5

        func(idx, d)

    for i in range(4):
        if magnet[i+1][0]:
            ans += 1<<i

    print("#{} {}".format(T, ans))