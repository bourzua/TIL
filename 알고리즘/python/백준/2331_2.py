import sys
A, P = map(int, sys.stdin.readline().split())

temp = [A]

while True:
    num = 0
    for n in str(temp[-1]):
        num += int(n)**P
    if num in temp:
        print(temp.index(num))
        break
    temp.append(num)