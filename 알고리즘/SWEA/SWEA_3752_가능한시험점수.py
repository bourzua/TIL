import sys
sys.stdin = open("3752.txt","r")

# 비트마스킹 실패(N이 너무 큼)

for T in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [1] + [0]*sum(arr)
    scores = [0]
    for i in arr:
        li = scores[:]
        for j in li:
            if not visited[i+j]:
                visited[i+j] = 1
                scores.append(i+j)
    ans = len(scores)
    print("#{} {}".format(T, ans))