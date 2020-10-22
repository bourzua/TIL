import sys
sys.stdin = open("4834.txt","r")

for T in range(1, int(input())+1):
    N = int(input())

    card = input()
    card = list(card)
    card = list(map(int, card))

    a = max(card)

    theNumberOf = [0]*(a+1)

    for i in card:
        theNumberOf[i] += 1

    MAX = 0
    number = 0
    for i in range(len(theNumberOf)):
        if theNumberOf[i] >= MAX:
            MAX = theNumberOf[i]
            number = i

    print("#{} {} {}".format(T, number, MAX))