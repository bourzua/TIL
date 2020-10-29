import sys
sys.stdin = open("5185.txt", "r")

for T in range(1, int(input())+1):
    N, HEX = input().split()
    HEX = int(HEX, 16)
    # 접두어 빼고 보여줌
    HEX = format(HEX, 'b')
    # 맨 앞이 0이면 안나오니까
    if len(HEX) != int(N)*4:
        HEX = '0'*(int(N)*4 - len(HEX)) + HEX
    print("#{} {}".format(T, HEX))