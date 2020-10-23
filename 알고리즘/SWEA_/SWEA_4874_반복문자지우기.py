import sys
sys.stdin = open("4874.txt","r")

for T in range(1, int(input())+1):
    word = input()
    word = list(word)

    stack = []

    for i in range(len(word)):
        if len(stack) == 0:
            stack.append(word[i])
        else:
            if stack[-1] == word[i]:
                stack.pop()
            else:
                stack.append(word[i])

    print("#{} {}".format(T, len(stack)))