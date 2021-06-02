# 처음과 끝, 잘리는 위치를 리스트에 넣은 후 정렬한다.
# 2개 씩 차이를 리스트에 담는다.
# 가로 차이 리스트와 세로 차이 리스트를 곱해준 것 중 가장 큰 것을 출력한다.
# 가로로 자르면 세로리스트에 추가되고, 세로로 자르면 가로리스트에 추가되는 게 헷갈렸다.

# 가로, 세로
w, h = map(int, input().split())
N = int(input())

wList = [0, w]
hList = [0, h]

for _ in range(N):
    a, b = map(int, input().split())
    # 가로로 자르면 세로리스트에 추가
    if a == 0:
        hList.append(b)
    else:
        wList.append(b)

wList.sort()
hList.sort()

wList2 = []
hList2 = []

for i in range(len(wList)-1):
    minus = wList[i+1] - wList[i]
    wList2.append(minus)
for i in range(len(hList)-1):
    minus = hList[i+1] - hList[i]
    hList2.append(minus)


MAX = 0

for i in range(len(wList2)):
    for j in range(len(hList2)):
        if wList2[i]*hList2[j] >MAX:
            MAX = wList2[i]*hList2[j]

print(MAX)