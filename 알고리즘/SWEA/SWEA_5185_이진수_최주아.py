def binary(n):
    global binList
    for i in range(3, -1, -1):
        a = n // 2**i
        binList.append(a)
        n = n - a*(2**i)



for T in range(1, int(input())+1):
    N, hex = input().split()

    N = int(N)

    binList = []

    for i in range(N):
        if hex[i] == 'A':
            binary(10)
        elif hex[i] == 'B':
            binary(11)
        elif hex[i] == 'C':
            binary(12)
        elif hex[i] == 'D':
            binary(13)
        elif hex[i] == 'E':
            binary(14)
        elif hex[i] == 'F':
            binary(15)
        else:
            binary(int(hex[i]))
    ans = ''
    for i in range(len(binList)):
        ans += str(binList[i])
    print("#{} {}".format(T, ans))