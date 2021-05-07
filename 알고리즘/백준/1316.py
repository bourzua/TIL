N = int(input())
ans = 0

for _ in range(N):
    word = input()
    al = set()
    flag = True
    for i in range(len(word)):
        if word[i] not in al:
            al.add(word[i])
        elif word[i] in al:
            if word[i] != word[i-1]:
                flag = False
                break
    if flag == False:
        continue
    ans += 1

print(ans)