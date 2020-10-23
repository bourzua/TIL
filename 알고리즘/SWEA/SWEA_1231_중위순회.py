import sys
sys.stdin = open("1231.txt","r")

def inorder(node):
    global ans
    if node:
        # 왼쪽자식 있으면 있는만큼 끝까지 내려가
        inorder(tree[node][0])
        # 마지막노드에서 왼쪽 없으니까 가운데인 자신 출력
        ans += word[node]
        # 이제 오른쪽 확인
        inorder(tree[node][1])


for T in range(1, 11):
    # 입력받는게 어려웠는데 결국 노가다로
    V = int(input())
    # [왼쪽자식,오른쪽자식,부모]
    tree = [[0]*3 for _ in range(V+1)]
    # N번 노드에 어떤 문자열이 담겼는지
    word = [0]*(V+1)
    ans = ''
    for i in range(1, V+1):
        # 일단 편하게 str로 받고
        info = input().split()
        # 두번째 원소는 word에 저장
        word[i] = info[1]
        # 세번째 원소가 있다면 왼쪽자식이 있는 것
        if len(info)>=3:
            left = int(info[2])
            tree[i][0] = left
            tree[left][2] = i
        # 네번째 원소가 있다면 오른쪽자식이 있는 것
        if len(info)>=4:
            right = int(info[3])
            tree[i][1] = right
            tree[right][2] = i
    inorder(1)
    print("#{} {}".format(T, ans))