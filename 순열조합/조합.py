# 5C3

arr = ['A', 'B', 'C', 'D', 'E']
N = len(arr)

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(arr[i], arr[j], arr[k])