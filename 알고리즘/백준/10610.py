# 순열인줄 알았는데 그냥 수학문제였음..
# 숫자로 접근하면 초과 나니까 str로 접근

N = input()
N = sorted(N, reverse=True)
sum = 0

# 이렇게 했는데 N이 최대 10의 5승개의 숫자로 구성되어 있으므로 힘듦
# while N > 0:
#     a = N % 10
#     numList.append(a)
#     N = N // 10

# 0이 무조건 있어야 함
if '0' in N:
    for i in N:
        sum += int(i)
    # 0이 있을 때 각 자리의 합 3으로 나누어떨어져야함
    if sum%3 == 0:
        print(''.join(N))
    else:
        print(-1)
else:
    print(-1)