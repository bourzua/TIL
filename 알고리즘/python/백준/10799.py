# import sys
#
# ps = sys.stdin.readline()

ps = input()

ans = 0
stack = []

for i in range(len(ps)):
    if ps[i] == '(':
        stack.append('(')
    else:
        if ps[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1

print(ans)