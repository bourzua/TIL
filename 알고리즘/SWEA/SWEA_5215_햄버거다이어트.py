import sys
sys.stdin = open("5215.txt", "r")

for T in range(1, int(input())+1):
    N, L = map(int, input().split())

    score, calorie = [], []

    for _ in range(N):
        s, c = map(int, input().split())
        score.append(s)
        calorie.append(c)

    ans = 0
    # 비트연산을 통한 모든 부분집합 구하기
    for i in range(1<<N):
        sum_score = 0
        sum_calorie = 0
        for j in range(N):
            if i & (1<<j):
                sum_calorie += calorie[j]
                sum_score += score[j]
        # i번째 햄버거의 맛과 칼로리를 모두 계산한 결과
            if sum_calorie <= L:
                ans = max(ans, sum_score)

    print("#{} {}".format(T, ans))