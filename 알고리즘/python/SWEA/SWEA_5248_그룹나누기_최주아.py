import sys
sys.stdin = open("5248.txt", "r")

def findset(x):
    while x != parent[x]:
        x = parent[x]
    return x

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    List = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    # 튜플 담을 리스트
    likes = []

    # for i in range(0, len(List), 2):
    #     relation.append(List[i], List[i+1])

    # 튜플 넣어주기
    for i in range(M):
        likes.append((List[2*i],List[2*i+1]))

    # 부모 끝까지 찾기
    for like in likes:
        # 부모 타고 들어가서 바꾸면 전체에서 -1되는 거니까
        # 한 그룹이면 합쳐야 함
        parent[findset(like[1])] = findset(like[0])

    count = 0

    for i in range(1, N+1):
        if parent[i] == i:
            count += 1

    print("#{} {}".format(T, count))