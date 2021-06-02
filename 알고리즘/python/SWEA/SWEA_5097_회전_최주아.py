import sys
sys.stdin = open("5097.txt","r")

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    for i in range(M):
        tmp = queue.pop(0)
        queue.append(tmp)

    print("#{} {}".format(T, queue[0]))