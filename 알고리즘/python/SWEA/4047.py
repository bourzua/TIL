import sys
sys.stdin = open("4047.txt", "r")

for T in range(1, int(input())+1):
    onecard = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    ans = ''
    question = input()
    cardList = []
    for i in range(0, len(question), 3):
        card = question[i:i+3]
        cardList.append(card)
    if len(cardList) != len(set(cardList)):
        ans = 'ERROR'
    else:
        for i in cardList:
            onecard[i[0]] -= 1

    if ans == 'ERROR':
        print("#{} {}".format(T, ans))
    else:
        print("#{}".format(T), end=" ")
        for i in onecard:
            if i == 'C':
                print(onecard[i])
            else:
                print(onecard[i], end=" ")
