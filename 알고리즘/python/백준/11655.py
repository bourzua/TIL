import sys
S = list(sys.stdin.readline().rstrip('\n'))

ans = ''

for i in S:
    if i.islower():
        if ord(i) + 13 <= ord('z'):
            ans += chr(ord(i) + 13)
        else:
            ans += chr(ord(i) + 13 - 26)

    elif i.isupper():
        if ord(i) + 13 <= ord('Z'):
            ans += chr(ord(i) + 13)
        else:
            ans += chr(ord(i) + 13 - 26)

    else:
        ans += i

print(ans)