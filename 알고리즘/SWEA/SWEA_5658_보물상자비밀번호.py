import sys
sys.stdin = open("5658.txt", "r")

# 문자열 맨뒤를 맨앞으로
def change():
    global box
    box1 = box[0:len(box)-1]
    box2 = box[len(box)-1:]
    box = box2 + box1

for T in range(1, int(input())+1):
    N, K = map(int, input().split())
    L = N // 4

    box = input()

    # 중복 제거를 위해 처음에 set 사용
    numbers = set()
    # N//4번만큼 회전하니까
    for _ in range(L):
        # N//4 길이만큼 잘라서 set에 넣기
        for i in range(0, N, L):
            add = box[i:i+L]
            numbers.add(add)
        change()

    numbers = list(numbers)
    # 내림차순
    numbers.sort(reverse=True)
    # K번째
    ans = numbers[K-1]
    ans = int(ans, 16)

    print('#{} {}'.format(T, ans))
