import sys
sys.stdin = open("4866.txt","r")

for T in range(1, int(input())+1):
    check = input()
    ans = 0
    flag = False

    list = []

    for i in range(len(check)):
        if check[i] == '(' or check[i] == '{':
            list.append(check[i])
        elif check[i] == ')':
            if len(list) == 0:
                flag = True
                break
            else:
                if list[-1] == '(':
                    list.pop()
                else:
                    flag = True
                    break
        elif check[i] == '}':
            if len(list) == 0:
                flag = True
                break
            else:
                if list[-1] == '{':
                    list.pop()
                else:
                    flag = True
                    break

    if flag == False and len(list) == 0:
        ans = 1

    print("#{} {}".format(T, ans))
