# lomuto-partition
import sys
sys.stdin = open("5205.txt","r")

def quick_sort(numList, l, r):
    if l < r:
        p=partition(numList, l, r)
        quick_sort(numList, l, p-1)
        quick_sort(numList, p+1, r)

# 맨 마지막 값을 피봇으로
def partition(numList, l, r):
    pivot = numList[r]
    i = l - 1
    for j in range(l, r):
        if numList[j] <= pivot:
            i += 1
            numList[i], numList[j] = numList[j], numList[i]
    numList[i + 1], numList[r] = numList[r], numList[i + 1]
    return i + 1

for T in range(1, int(input())+1):
    N = int(input())
    numList = list(map(int, input().split()))


    quick_sort(numList, 0, N-1)
    print("#{} {}".format(T, numList[N//2]))