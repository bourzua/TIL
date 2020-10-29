arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

N = len(arr)

sel = [0] * N

def powerset(idx):
    global selectList
    if idx == N:
        total = 0
        select = []
        for i in range(N):
            if sel[i]:
                total += arr[i]
                select.append(arr[i])
        if total == 0:
            selectList.append(select)
        return

    sel[idx] = 1
    powerset(idx + 1)

    sel[idx] = 0
    powerset(idx + 1)

selectList = []
powerset(0)

for i in selectList:
    print(i)