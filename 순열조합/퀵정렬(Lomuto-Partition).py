# 가장 오른쪽 자리를 피봇으로 설정
list = [11, 45, 23, 81, 28, 34]

pivot = list[-1]
i = -1
j = 0

while(j<len(list)-1):
    if(list[j] <= pivot):
        i += 1
        list[i], list[j] = list[j], list[i]
    j += 1

list[i+1], list[-1] = list[-1], list[i+1]

print(list)