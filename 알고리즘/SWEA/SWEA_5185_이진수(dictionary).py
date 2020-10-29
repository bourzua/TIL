import sys
sys.stdin = open("5185.txt", "r")

b_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
          'D': 13, 'E': 14, 'F': 15}
binary = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011',
          '1100', '1101', '1110', '1111']

for T in range(1, int(input())+1):
    N, HEX = input().split()
    ans = ''

    for i in HEX:
        ans += binary[b_dict[i]]
    print("#{} {}".format(T, ans))