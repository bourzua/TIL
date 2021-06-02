from itertools import combinations

nums =[1, 2, 3, 4, 5]
A = list(combinations(nums,3))
for i in range(len(A)):
    A[i] = sum(A[i])
print(A)