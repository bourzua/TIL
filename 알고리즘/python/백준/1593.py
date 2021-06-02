import sys
g, s = map(int, sys.stdin.readline().split())
W = sys.stdin.readline().rstrip()
S = sys.stdin.readline().rstrip()

wl = [0]*52
sl = [0]*52

for i in W:
    if 'a' <= i <= 'z':
        wl[ord(i) - ord('a')] += 1
    else:
        wl[ord(i) - ord('A')+26] += 1

start, end, ans = 0, 0, 0
for i in range(s):
    if 'a' <= S[i] <= 'z':
        sl[ord(S[i]) - ord('a')] += 1
    else:
        sl[ord(S[i]) - ord('A')+26] += 1
    end += 1

    if end == g:
        if sl == wl:
            ans += 1
        if 'a' <= S[start] <= 'z':
            sl[ord(S[start]) - ord('a')] -= 1
        else:
            sl[ord(S[start]) - ord('A') + 26] -= 1
        start += 1
        end -= 1
print(ans)