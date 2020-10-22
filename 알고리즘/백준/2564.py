def length(a, b, c, d):
    if a == 3:
        return b
    elif a == 2:
        return d+b
    elif a == 4:
        return d+c+d-b
    else:
        return d+c+d+c-b


garo, sero = map(int,input().split())

N = int(input())
list = []

for i in range(N):
    a, b = map(int, input().split())
    list.append(length(a,b,garo,sero))

realA, realB = map(int, input().split())
where = length(realA, realB, garo, sero)
sum = 0

for i in list:
    if abs(i-where) < garo + sero:
        sum += abs(i-where)
    else:
        sum += 2*(garo+sero) - abs(i-where)

print(sum)