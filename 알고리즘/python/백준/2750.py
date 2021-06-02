def mergeSort(list):
    if len(list) == 1:
        return list
    middle = len(list) // 2

    leftList = list[:middle]
    rightList = list[middle:]

    leftList = mergeSort(leftList)
    rightList = mergeSort(rightList)

    return merge(leftList, rightList)

def merge(left, right):

    i = 0
    j = 0
    tmp = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1

    while i < len(left):
        tmp.append(left[i])
        i += 1

    while j < len(right):
        tmp.append(right[j])
        j += 1

    return tmp


N = int(input())
numList = []

for i in range(N):
    numList.append(int(input()))

newList = mergeSort(numList)
print(*newList, sep="\n")

