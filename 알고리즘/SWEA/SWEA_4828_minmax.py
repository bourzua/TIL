import sys
sys.stdin = open("4828.txt","r")

for T in range(1, int(input()) + 1):
    N = input()
    numberList = list(map(int, input().split()))

    MAX = 0
    MIN = 1000000
    for i in numberList:
        if i > MAX:
            MAX = i
        if i < MIN:
            MIN = i

    print("#{} {}".format(T, MAX-MIN))