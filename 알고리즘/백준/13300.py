N, K = map(int, input().split())

girlsCount = [0]*7
boysCount = [0]*7

for T in range(N):
    gender, grade = map(int, input().split())
    if gender == 0:
        girlsCount[grade] += 1
    else:
        boysCount[grade] += 1

count = 0
for i in range(1, 7):
    if girlsCount[i]%K == 0:
        count += girlsCount[i]//K
    elif girlsCount[i]%K != 0:
        count += girlsCount[i]//K + 1
    if boysCount[i] % K == 0:
        count += boysCount[i] // K
    elif boysCount[i]%K != 0:
        count += boysCount[i]//K + 1

print(count)