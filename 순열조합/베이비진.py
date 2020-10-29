def perm(n, k):
    global ans
    if n == k:
        count = 0
        for i in range(0, k, 3):
            B = A[i:i+3]
            # print(B)
            if B[0] == B[1] == B[2] or B[2] - B[1] == B[1] - B[0] == 1 or B[0] - B[1] == B[1] - B[2] == 1:
                count +=1
            if count == 2:
                ans = 'babygin!'
                return
    else:
        for i in range(n, k):
            A[n], A[i] = A[i], A[n]
            perm(n+1, k)
            A[n], A[i] = A[i], A[n]

N = input()
K = len(N)
A = []

for i in range(K):
     A.append(int(N[i]))

ans = 'not babygin'

perm(0,K)

print(ans)