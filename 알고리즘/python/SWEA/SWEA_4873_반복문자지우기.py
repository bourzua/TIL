import sys
sys.stdin = open("4873.txt", "r")

for T in range(1, int(input())+1):
    word = list(input())

    stack = []

    for i in range(len(word)):
        # 없으면 넣고
        if len(stack) == 0:
            stack.append(word[i])
        # 있으면 이전이랑 같으면 빼고 아니면 넣고
        else:
            if stack[-1] == word[i]:
                stack.pop()
            else:
                stack.append(word[i])

    print("#{} {}".format(T, len(stack)))