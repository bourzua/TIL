import sys
sys.stdin = open("5203.txt", "r")

def perm(n, k, player, playerList):
    if n == k:
        # 앞에 3개 자르기
        playerList.append(player[0:3])
    else:
        for i in range(n, k):
            player[n], player[i] = player[i], player[n]
            perm(n+1, k, player, playerList)
            player[n], player[i] = player[i], player[n]


def check(i):
    global count
    if i[0] == i[1] == i[2] or i[2] - i[1] == i[1] - i[0] == 1 or i[0] - i[1] == i[1] - i[2] == 1:
        count += 1
        return


for T in range(1, int(input())+1):
    numList = list(map(int, input().split()))
    player1 = []
    player2 = []
    ans = 0

    # player 리스트에 각각 하나씩 넣기
    for i in range(0, 11, 2):
        count = 0
        player1.append(numList[i])
        # print(player1)
        player2.append(numList[i+1])
        # print(player2)
        # 3개부터 체크하기
        if len(player1) >= 3:
            # 체크할 조합들을 모을 리스트 생성
            playerList1 = []
            k = len(player1)
            # 온갖 조합 중 앞에 3개 자른 것 리스트에 넣기
            perm(0, k, player1, playerList1)
            newPlayerList1 = []
            # 중복 제거
            for i in playerList1:
                if i not in newPlayerList1:
                    newPlayerList1.append(i)

            # 체크해주기
            for i in newPlayerList1:
                check(i)
                # 한 개라도 발견하면 바로 나오기
                if count == 1:
                    ans = 1
                    break
        if ans == 1:
            break

        if len(player2) >= 3:
            playerList2 = []
            k = len(player2)
            perm(0, k, player2, playerList2)
            newPlayerList2 = []
            for i in playerList2:
                if i not in newPlayerList2:
                    newPlayerList2.append(i)
            for i in newPlayerList2:
                check(i)
                if count == 1:
                    ans = 2
                    break
        if ans == 2:
            break

    print("#{} {}".format(T, ans))
