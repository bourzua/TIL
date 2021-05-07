import sys
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

memory = sys.stdin.readline().rstrip()
ans = 0
for i in memory:
    for j in dial:
        if i in j:
            ans += dial.index(j) + 3

print(ans)