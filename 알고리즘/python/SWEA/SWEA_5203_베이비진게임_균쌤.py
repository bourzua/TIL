import sys
sys.stdin = open("5203.txt", "r")

def check(p, idx):
    # triplet?
    if p[idx] >= 3:
        return True
    # run?
    for i in range(1, 9):
        if p[i-1] and p[i] and p[i+1]:
            return True



for T in range(1, int(input())+1):
    card = list(map(int, input().split()))
    # 나온 카드 count
    player1 = [0]*10
    player2 = [0]*10

    win = 0

    for i in range(0, len(card), 2):
        player1[card[i]] += 1
        player2[card[i+1]] += 1
        # 카드 3장부터 유효하니까
        if i >= 4:
            flag1 = check(player1, card[i])
            flag2 = check(player2, card[i+1])

            if flag1:
                win = 1
                break
            elif flag2:
                win = 2
                break

    print("#{} {}".format(T, win))