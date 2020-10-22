import sys
sys.stdin = open("1204.txt","r")

for T in range(1, int(input())+1):
    N = int(input())

    count = [0]*101
    answer = 0

    studentScore = list(map(int, input().split()))


    for score in studentScore:
        count[score] += 1

    MAX = max(count)

    answerList = []

    for i in range(101):
        if count[i] == MAX:
            answerList.append(i)



    if len(answerList) == 1:
        answer = answerList[0]
    elif len(answerList) > 1:
        answer = max(answerList)

    print("#{} {}".format(T, answer))