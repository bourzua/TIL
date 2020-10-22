# 시작위치, 길이, 이동횟수
def where(now, length, number):
    # 길이의 2배만큼 가면 원상태로 돌아옴 => 나머지만큼만 가자
    nt = number % (2*length)
    # 방향
    flag = 1

    for i in range(nt):
        # 맨 왼쪽이나 맨 오른쪽에 닿으면 방향 바꿈
        if now == 0 or now == length:
            flag *= -1
        # 방향 변경 여부 상관없이 한칸이동
        now += flag

    return now

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = where(p,w,t)
y = where(q,h,t)

print(x,y)