import sys
sys.stdin = open("5099.txt","r")

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    cheese = [0] + list(map(int, input().split()))

    fire = [i for i in range(1,N+1)]
    next = N+1

    while len(fire)>1:
        num = fire.pop(0)
        cheese[num] = cheese[num]//2
        if cheese[num]>0:
            fire.append(num)
        else:
            if next <= M:
                fire.append(next)
                next += 1
    print("#{} {}".format(T, fire[0]))