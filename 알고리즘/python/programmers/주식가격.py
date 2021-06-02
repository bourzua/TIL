def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        a = prices[i]
        time = 0
        for j in range(i+1, len(prices)):
            if prices[j] >= a:
                time += 1
            else:
                time +=1
                break
        answer.append(time)
    answer.append(0)

    return answer

ex_array = [1, 2, 3, 2, 3, 1]
ans = solution(ex_array)

print(ans)