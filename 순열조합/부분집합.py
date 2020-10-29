N = 10

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sel = [0] * N

def powerset(idx):
    # 도착을 했을때
    if idx == N:
        print(sel)
        total = 0
        #뽑은 것들의 합을 구함
        for i in range(N):
            if sel[i]:
                total += arr[i]
        #합이 10일때 경우만 출력
        # if total == 10:
            # print(sel)
        return

    # 해당자리를 뽑고 가고
    sel[idx] = 1
    powerset(idx + 1)
    # 해당자리를 안뽑고 가고
    sel[idx] = 0
    powerset(idx + 1)


powerset(0)