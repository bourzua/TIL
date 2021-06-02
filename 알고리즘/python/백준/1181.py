# 처음부터 중복 안되게!
N = int(input())

wl = set()

for _ in range(N):
    wl.add(input())

wl = list(wl)
wl.sort()
wl.sort(key=lambda x:len(x))

for i in wl:
    print(i)