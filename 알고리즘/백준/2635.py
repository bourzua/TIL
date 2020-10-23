N = int(input())
# 정답 리스트
list1 = []

MAX = 0

# N 자신부터 1까지 다 해보기
for i in range(N, 0, -1):
    # 원래 N은 포함이 되므로 포함하고 시작
    list2 = [N]
    # i가 두번째 값
    K = i
    # (마지막에서 두번째 - 마지막)값은 음수면 안됨
    while K >=0:
        # 뺀 값 넣고
        list2.append(K)
        # 새로운 뺀 값 설정
        K = list2[len(list2)-2]-list2[len(list2)-1]
    # 완성된 리스트 길이가 이전보다 클때
    if len(list2) > MAX:
        # 그 리스트를 정답리스트에 할당한 후
        list1 = list2[:]
        # 최대 길이 갱신
        MAX = len(list1)

print(len(list1))
print(*list1)