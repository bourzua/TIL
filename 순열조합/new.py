calList = list(input().split())
stack = []
ans = 0
for i in range(len(calList)):
    if calList[i].isdigit():
        stack.append(int(calList[i]))
    elif calList[i] == '.':
        if len(stack) != 1:
            ans = 'error'
            break
        ans = stack.pop()
    else:
        if len(stack) == 0 or len(stack) == 1:
            ans = 'error'
            break
        b = stack.pop()
        a = stack.pop()
        if calList[i] == '+':
            c = a + b
            stack.append(c)
        elif calList[i] == '-':
            c = a - b
            stack.append(c)
        elif calList[i] == '/':
            c = a / b
            stack.append(c)
        else:
            c = a * b
            stack.append(c)

print(ans)