import sys
sys.stdin = open("1215.txt","r")

for T in range(1, 11):
    N = int(input())
    rec = [list(input()) for _ in range(8)]

    count = 0

    for i in range(8):
        for j in range(8-N+1):
            words = []
            for a in range(N):
                words.append(rec[i][j+a])
            if words == words[::-1]:
                count += 1

    for i in range(8-N+1):
        for j in range(8):
            words = []
            for a in range(N):
                words.append(rec[i+a][j])
            if words == words[::-1]:
                count += 1


    print("#{} {}".format(T, count))