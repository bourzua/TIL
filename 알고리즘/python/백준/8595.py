N = int(input())
S = input()
ans = 0

num = ''
for i in S:
    if i.isnumeric():
        num += i
    else:
        if num:
            ans += int(num)
            num = ''

if num:
    ans += int(num)

print(ans)