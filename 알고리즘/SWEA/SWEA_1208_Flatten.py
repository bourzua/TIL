import sys
sys.stdin = open("1208.txt","r")

for T in range(1, 11):
    number = int(input())

    box = list(map(int, input().split()))
    box.sort()

    for _ in range(number):
        box[-1] -= 1
        box[0] += 1
        box.sort()

    answer = max(box) - min(box)

    print("#{} {}".format(T, answer))