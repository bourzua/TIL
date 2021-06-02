import sys
sys.stdin = open("1231.txt","r")

def inorder(v):
    global ans
    if v > N:
        return
    inorder(2*v)
    ans += word[v]
    inorder(2*v + 1)


for T in range(1, 11):
    N = int(input())
    word = [0]*(N+1)
    for i in range(1, N+1):
        hint = list(input().split())
        word[i] = hint.pop(1)

    ans = ''
    inorder(1)
    print("#{} {}".format(T, ans))