import sys
sys.stdin = open("5249.txt", "r")

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

for T in range(1, int(input()+1)):
    V, E = map(int, input().split())

    for _ in range(M):
