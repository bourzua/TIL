N = int(input())
numList = list(map(int, input().split()))
count = 0

for i in numList:
    if i == 1:
        continue
    elif i == 2:
        count += 1
    else:
        check = 0
        for j in range(2, i):
            if i%j == 0:
                check = 1
                break
        if check == 0:
            count += 1

print(count)