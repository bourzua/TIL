nine = []
visited = []
for _ in range(9):
    nine.append(int(input()))

sel = [0]*9

def powerset(idx):
    global visited
    if idx == 9:
        total = 0
        # 7개가 뽑힌 경우마다 합을 구해줌
        if sel.count(1) == 7:
            for i in range(9):
                if sel[i]:
                    total += nine[i]
            # 합이 100이면 그때의 방문list 가지고 나오기
            if total == 100:
                # list는 이렇게 복사해야함!
                visited = sel[:]
        return
    # 해당자리를 뽑고 가고
    sel[idx] = 1
    powerset(idx + 1)
    # 해당자리를 안뽑고 가고
    sel[idx] = 0
    powerset(idx + 1)


powerset(0)

seven = []
for i in range(9):
    if visited[i] == 1:
        seven.append(nine[i])

seven.sort()

for i in range(len(seven)):
    print(seven[i])