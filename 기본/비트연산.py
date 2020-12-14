food = ["상추", "고기", "토마토", "치즈", "피클"]
N = len(food)

for i in range(1<<N):
    tmp = "햄버거 : "
    for j in range(N):
        if i & (1<<j):
            tmp += food[j] + " "

    print(i, bin(i), tmp)