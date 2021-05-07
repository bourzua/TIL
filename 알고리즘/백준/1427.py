s = input()
numList = [int(i) for i in s]

numList.sort(reverse=True)
for i in numList:
    print(i, end='')