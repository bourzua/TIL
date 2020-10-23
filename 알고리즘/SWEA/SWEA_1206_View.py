import sys
sys.stdin = open("1206.txt", "r")

for T in range(1, 11):
    length = int(input())
    building = list(map(int, input().split()))
    count = 0

    for i in range(2, length - 2):
        MAX = max((building[i-2]), building[i-1], building[i+1], building[i+2])
        if building[i] > MAX:
            count += building[i] - MAX


    print("#{} {}".format(T, count))