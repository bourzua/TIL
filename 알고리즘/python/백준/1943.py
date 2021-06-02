# 유클리드 호제법
import sys

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)
N = int(sys.stdin.readline())
while N:
    a, b = map(int, sys.stdin.readline().split())
    print(a*b//gcd(a, b))
    N -= 1