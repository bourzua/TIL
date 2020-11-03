import sys
sys.stdin = open("5204.txt","r")

def merge_sort(list):
    # 종료조건
    if len(list) == 1:
        return list
    middle = len(list) // 2

    leftList = list[:middle]
    rightList = list[middle:]

    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)

def merge(left, right):
    global count
    global ans
    i = 0
    j = 0
    tmp = []
    if left[-1] > right[-1]:
        count += 1
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    while i < len(left):
        tmp.append(left[i])
        i+=1
    while j < len(right):
        tmp.append(right[j])
        j+=1

    return tmp

for T in range(1, int(input())+1):
    N = int(input())

    numList = list(map(int, input().split()))
    count = 0
    ans = 0
    numList=merge_sort(numList)

    N = len(numList) // 2
    ans = numList[N]
    print("#{} {} {}".format(T, ans, count))