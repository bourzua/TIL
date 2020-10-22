def check(arr):
    global ans
    cnt = 1
    for i in range(1, N):
        if arr[i-1] <= arr[i]:  cnt += 1
        else:   cnt = 1

        if ans < cnt:   ans = cnt



N = int(input())
numList = list(map(int, input().split()))

ans = 1
check(numList)
check(numList[::-1])
print(ans)