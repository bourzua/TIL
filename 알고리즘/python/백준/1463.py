a = int(input())
count = 0

while a != 1:
    count += 1
    if a%3 == 0:
        a = a / 3
    elif a%2 == 0:
        a = a / 2
    else:
        a = a - 1
print(count)
