def inorder(v):
    if 2*v <= N:
        inorder(2*v)
    valueList[v] = values.pop(0)
    if 2*v+1 <=N:
        inorder(2*v+1)


for T in range(1, int(input())+1):
    N = int(input())

    valueList = [0]*(N+1)

    values = [i for i in range(1, N+1)]

    inorder(1)

    print("#{} {} {}".format(T,  ], valueList[N//2]))