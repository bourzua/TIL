for T in range(int(input())):

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    Anumber = [0]*5
    Bnumber = [0]*5

    A.pop(0)
    B.pop(0)

    for i in range(1, 5):
        Anumber[i] = A.count(i)
        Bnumber[i] = B.count(i)

    for i in range(4, 0, -1):
        Ai = Anumber[i]
        Bi = Bnumber[i]

        if Ai > Bi:
            print('A')
            break
        elif Ai < Bi:
            print('B')
            break
        elif i == 1:
            print('D')
