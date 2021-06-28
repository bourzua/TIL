def solution(progresses, speeds):
    answer = []

    for k in range(len(progresses)):
        progresses[k] = 100 - progresses[k]

    i = 0
    while i < len(progresses):
        k = 0
        divide = 0

        if progresses[i] % speeds[i] == 0:
            divide = progresses[i] // speeds[i]
        else:
            divide = progresses[i] // speeds[i] + 1

        for j in range(i + 1, len(progresses)):
            progresses[j] = progresses[j] - divide * speeds[j]

        for j in range(i + 1, len(progresses)):
            if progresses[j] <= 0:
                k += 1
            else:
                break

        answer.append(1 + k)
        i += (1 + k)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))