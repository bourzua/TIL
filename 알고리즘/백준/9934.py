# 인덱스 짝수칸만 => 맨 아랫줄
# 그거 뺴고 인덱스 짝수칸만 => 그 다음 아랫줄
#  ... 반복

N = int(input())
numList = list(map(int, input().split()))
visited = [0]*len(numList)

newList = []

while len(newList) < len(numList):
    K = 0
    for i in range(len(numList)):
        if visited[i]:
            continue
        K += 1
        if K % 2 == 1:
            visited[i] = 1
            newList.append(numList[i])

for i in range(N):
    for j in range(len(newList) - 2**(i+1) + 1, len(newList) - 2**i + 1):
        print(newList[j], end=" ")
    print()