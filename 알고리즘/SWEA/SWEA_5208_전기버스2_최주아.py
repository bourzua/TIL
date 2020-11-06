import sys
sys.stdin = open("5208.txt","r")

def check(my, cnt):
    global ans

    if cnt > ans:
        return

    if my >= bus_stop[0]:
        ans = min(ans, cnt)
        return

    for i in range(my + bus_stop[my], my, -1):
        check(i, cnt+1)

for T in range(1, int(input())+1):
    bus_stop = list(map(int, input().split()))
    ans = 0xfffffff
    check(1, -1)

    print("#{} {}".format(T, ans))