heightList = [0]*1001

valid = []

for T in range(1, int(input())+1):
    a, height = map(int, input().split())
    valid.append(a)
    heightList[a] = height

start = min(valid)
end = max(valid)

# highest = max(heightList)
# for i in range(start, end+1):
#     if heightList

MAX = 0
total = 0
for i in range(start, end + 1):
    if heightList[i]>MAX:
        MAX = heightList[i]
    total += MAX

MAX2 = 0
minustotal = 0

for i in range(end, start,-1):
    if heightList[i]>MAX2:
        MAX2 = heightList[i]
        if MAX2 == MAX:
            break
    minustotal += MAX-MAX2

print(total-minustotal)