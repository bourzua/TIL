A, B = map(int, input().split())
tmp = 0
bigger = 0
smaller = 0

ans1 = 0
ans2 = 0

if A < B:
    bigger = B
    smaller = A
else:
    bigger = A
    smaller = B

for i in range(B, 0, -1):
    if A%i == 0 and B%i == 0:
        print(i)
        print(i*(bigger//i)*(smaller//i))
        break