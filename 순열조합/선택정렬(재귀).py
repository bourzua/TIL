def SelectionSort(A, s):
    n = len(A)

    if s == n - 1: return
    minidx = s

    # s 인덱스와 비교해서 더 작은 값을 가진 인덱스가 있다면 두 개 바꿔주기
    for i in range(s, n):
        if A[minidx] > A[i]:
            minidx = i

    A[s], A[minidx] = A[minidx], A[s]

    SelectionSort(A, s + 1)


A = [2, 4, 6, 1, 9, 8, 7, 0]

SelectionSort(A, 0)

print(A)