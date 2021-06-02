import sys
sys.stdin = open("4873.txt", "r")



for T in range(1, int(input())+1):
    words = list(input())
    flag = True
    while flag:
        count = 0
        for i in range(len(words) - 1):
            if words[i] == words[i + 1]:
                count += 1
                for _ in range(2):
                    words.pop(i)
                break
        if count == 0: flag = False

    ans = len(words)

    print("#{} {}".format(T, ans))