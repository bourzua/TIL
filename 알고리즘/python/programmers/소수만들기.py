def solution(nums):
    from itertools import combinations
    answer = 0
    for a in combinations(nums,3):
        aSum = sum(a)
        for j in range(3, aSum):
            if aSum%j == 0:
                break
        else:
            answer += 1
    return answer

ans = solution([1, 2, 7, 6, 4])

print(ans)