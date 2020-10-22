import sys
sys.stdin = open("1216.txt","r")

for T in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))

    lengthList = []
    key = 1
    for X in range(100, -1,-1):
        for i in range(100):
            for j in range(100-X+1):
                words = ''
                words2 = ''
                for a in range(X):
                    words += arr[i][j+a]
                    words2 += arr2[i][j+a]
                if words == words[::-1] or words2 == words2[::-1]:
                    lengthList.append(X)
                    key = 0;break
            if key == 0:break
        if key == 0:break


    realMax = max(lengthList)

    print("#{} {}".format(tc, realMax))