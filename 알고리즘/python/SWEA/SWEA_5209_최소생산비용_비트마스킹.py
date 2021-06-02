import sys
sys.stdin = open("5209.txt", "r")
# idx는 제품번호
def check(visited, idx, result):
    global ans
    # 가지치기
    if result > ans:
        return
    # N = 7일 때
    # 10000000 - 1 = 1111111이니까
    # 이진수가 모두 1로 되있는 경우(= 모두 방문)를 표현
    if visited == (1 << N) - 1:
        ans = min(ans, result)
        return

    for i in range(N):
        # N = 3일 때
        # visited = 1 << 0일 때
        # 001 & 001: 이미 들렀으니까
        # 001 & 010: 안들렀음 => 0
        # 그럼 거기 들러 (011, idx+1, result + cost[idx][i])
        if visited & (1 << i): continue
        check(visited | 1 << i, idx + 1, result + cost[idx][i])


for tc in range(1, int(input()) + 1):
    N = int(input())

    cost = [list(map(int, input().split())) for _ in range(N)]

    ans = 987654321
    # 첫번째 제품을 모든공장에서 만들어 보고 출발시킴
    # 제품이 5개라면
    # 00001
    # 00010
    # 00100
    # 01000
    # 10000
    for i in range(N):
        # 1을 i칸 만큼
        check(1 << i, 1, cost[0][i])

    print("#{} {}".format(tc, ans))