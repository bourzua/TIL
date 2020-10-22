import sys
sys.stdin = open("3752.txt","r")

for T in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))
    scoreVisited = [1] + [0]*sum(score)

    score2 = [0]

    for i in score:
        for j in range(len(score2)):
            if not scoreVisited[i+score2[j]]:
                scoreVisited[i+score2[j]] = 1
                score2.append(i+score2[j])

    print("#{} {}".format(T,len(score2)))