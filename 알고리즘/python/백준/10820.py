import sys

while True:
    lines = sys.stdin.readline().rstrip('\n')

    if not lines:
        break

    l, u, d, s = 0, 0, 0, 0

    for i in lines:
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
        elif i.isdigit():
            d += 1
        else:
            s += 1

    print(l, u, d, s)