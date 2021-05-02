import sys

stack1 = list(sys.stdin.readline().rstrip())
stack2 = []
N = int(sys.stdin.readline())
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if len(stack1) == 0:
            continue
        else:
            stack2.append(stack1.pop())
    elif command[0] == 'D':
        if len(stack2) == 0:
            continue
        else:
            stack1.append(stack2.pop())
    elif command[0] == 'B':
        if len(stack1) == 0:
            continue
        else:
            stack1.pop()
    else:
        stack1.append(command[1])
ans = ''
for i in stack1:
    ans += i
for i in range(len(stack2)-1, -1, -1):
    ans += stack2[i]
print(ans)