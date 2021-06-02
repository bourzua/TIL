N = int(input())
maxList = []

for i in range(N):
    new = sorted(list(map(int, input().split())))
    price = 0

    if len(set(new)) == 1:
        price = 50000 + new[0]*5000
    elif len(set(new)) == 2:
        if new[1] == new[2]:
            price = 10000 + new[1]*1000
        else:
            price = 2000 + new[1]*500 + new[2]*500
    elif len(set(new)) == 3:
        for j in range(3):
            if new[j] == new[j+1]:
                price = 1000 + new[j]*100
    else:
        price = max(new)*100

    maxList.append(price)

print(max(maxList))