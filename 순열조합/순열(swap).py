def perm(n, k): # n: 숫자를 결정할 인덱스, (결정한 개수) k: 순열의 길이
    if n == k:
        print(A)
    else:
        for i in range(n, k):
            A[n], A[i] = A[i], A[n] # 현재 숫자 유지부터, 오른쪽 끝까지 교환
            perm(n+1, k) # 다음 자리 결정하러 이동
            A[n], A[i] = A[i], A[n] # 교환 전으로 복구

A = [1, 2, 3]
perm(0,3)