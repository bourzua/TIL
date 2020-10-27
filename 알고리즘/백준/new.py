import copy

def binary(number):
    global binList
    # 2진법으로 된 수를 10진법으로
    y = int(number, 2)
    N = len(number)
    number = list(number)

    for i in range(1, N):
        if number[i] == '0':
            corrected = copy.deepcopy(number)
            corrected[i] = '1'
            corrected = ''.join(corrected)
            binList.append(int(corrected, 2))
        else:
            corrected = copy.deepcopy(number)
            corrected[i] = '0'
            corrected = ''.join(corrected)
            binList.append(int(corrected, 2))
binList = []
binary('1010')
print(binList)