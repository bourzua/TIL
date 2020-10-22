import sys
sys.stdin = open("4874_2.txt","r")

for T in range(1, int(input())+1):
    cal = list(input().split())
    stack =[]
    check = 0

    for i in range(len(cal)-1):
        if cal[i].isdigit():
            stack.append(cal[i])
        else:
            try:
                num2, num1 = int(stack.pop()), int(stack.pop())

                if cal[i] == '+':
                    result = num1 + num2
                elif cal[i] == '-':
                    result = num1 - num2
                elif cal[i] == '*':
                    result = num1 * num2
                elif cal[i] == '/':
                    result = num1 // num2

                stack.append(result)

            except:
                check = 'error'

    if check == 0 and len(stack) == 1:
        print("#{} {}".format(T, stack.pop()))
    elif check == 'error' or len(stack) > 1:
        print("#{} error".format(T))