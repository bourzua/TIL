재료 = ['단무지', '햄', '참치']

N = len(재료)

for i in range(1 << N):
    for j in range(N):
        if i & (1 << j):
            print(재료[j], end=" ")
    print("김밥입니다.")