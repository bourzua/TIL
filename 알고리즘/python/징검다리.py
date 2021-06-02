def move(stone_num, count, summ):
    global result
    if stone_num > N:
        if count == 0:
            if summ > result: result = summ
        return
    move(stone_num + 1, count - 1, summ + stone[stone_num + 1])
    move(stone_num + 2, count - 1, summ + stone[stone_num + 2])
for T in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    stone = [0] + list(map(int, input().split())) + [0, 0]
    result = 0
    move(0, M + 1, 0)
    print('#{} {}'.format(T, result))