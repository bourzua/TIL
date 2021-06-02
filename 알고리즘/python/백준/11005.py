import sys
N, B = map(int, sys.stdin.readline().split())
system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''

while N:
    ans += system[N%B]
    N = N//B

print(ans[::-1])