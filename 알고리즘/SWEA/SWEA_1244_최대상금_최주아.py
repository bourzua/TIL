import sys
sys.stdin = open("1244.txt", "r")

def backtrack(k):
    global ans
    num = int(''.join(map(str, a)))
    if num in visit[k]:
        return
    visit[k].add(num)
    if k == b:
        if ans < num:
            ans = num

    else:
        for i in range(N-1):
            for j in range(i+1, N):
                a[i], a[j] = a[j], a[i]
                backtrack(k+1)
                a[i], a[j] = a[j], a[i]

for T in range(1, int(input())+1):
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