def boy(X):
    for i in range(1, N+1):
        if i % X == 0:
            if switch[i]:
                switch[i] = 0
            else:
                switch[i] = 1

def girl(X):
    # 일단 지정위치 스위치 바꾸고
    if switch[X] == 0:
        switch[X] = 1
    else:
        switch[X] = 0

    # 양옆으로 옮길 수 있는 길이 구하자
    # 현재위치에서 양끝차이 중 작은 횟수가 최대임
    move = min(N-X, X-1)
    for i in range(1, move+1):
        # 양옆 같다면 바꾸기 진행
        if switch[X-i] == switch[X+i]:
            if switch[X-i] == 0:
                switch[X-i] = switch[X+i] = 1
            else:
                switch[X-i] = switch[X+i] = 0
        # 같지 않다면 멈춰
        else:
            break


N = int(input())
switch = [0] +list(map(int, input().split()))
K = int(input())

for i in range(K):
    gender, X = map(int, input().split())
    if gender == 1:
        boy(X)
    else:
        girl(X)

for i in range(1, N + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()