import sys
sys.stdin = open("4012.txt","r")

for T in range(1, int(input())+1):
    N = int(input())

    S = [list(map(int, input().split())) for _ in range(N)]

    numbers = []
    for i in range(N):
        numbers.append(i)

