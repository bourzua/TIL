import sys
sys.stdin = open("1244.txt", "r")

def backtrack(k):
    global ans
    # 리스트원소들 숫자로 바꿔주기
    num = int(''.join(map(str, a)))
    # 이미 있는 숫자면 리턴
    if num in visit[k]:
        return
    # 아니면 넣기
    visit[k].add(num)
    # 주어진 횟수만큼 교환하면 값 비교
    if k == b:
        if ans < num:
            ans = num
    else:
        # 조합
        for i in range(N-1):
            for j in range(i+1, N):
                a[i], a[j] = a[j], a[i]
                backtrack(k+1)
                a[i], a[j] = a[j], a[i]

for T in range(1, int(input())+1):
    # 최대 10번 교환하니까 10번째 세트까지 만들어주기
    visit = [set() for _ in range(11)]
    ans = 0
    a, b = input().split()
    a = list(a)
    b = int(b)
    N = len(a)
    backtrack(0)
    print("#{} {}".format(T, ans))

#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645