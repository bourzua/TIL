word = 'abcdabcdkk'
n = 10

remain = True
ans = 0

while True:
    if remain:
        if n%2 == 0 and word[:n//2] == word[n//2:]:
            remain = False
            ans += 1
            word = word[:n//2]
            n //= 2
        else:
            word = word[:n-1]
            ans += 1
            n -= 1
    else:
        ans += len(word)
        break

print(ans)
