import sys
sys.stdin = open("1211.txt", "r")

for i in range(1, int(input())+1):
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if ladder[0][i] == 1:
            