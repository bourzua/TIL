import sys
sys.stdin = open("4047.txt","r")

for T in range(1, int(input())+1):
    cards = input()
    result =''
    S = 13
    D = 13
    H = 13
    C = 13

    cardList = [cards[i:i+3] for i in range(0,len(cards),3)]

    cardSet = set(cardList)

    if len(cardList) != len(cardSet):
        result = 'ERROR'
        print("#{} {}".format(T, result))
    else:
        for i in cardList:
            if i[0] == 'S':
                S -= 1
            elif i[0] == 'D':
                D -= 1
            elif i[0] == 'H':
                H -= 1
            elif i[0] == 'C':
                C -= 1

        print("#{} {} {} {} {}".format(T, S, D, H, C))