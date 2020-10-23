def preorder(node):
    if node:
        print(node, end=" ")
        preorder(tree[node][0])
        preorder(tree[node][1])


V = int(input())  # 정점
E = V - 1  # 간선
tree = [[0] * 3 for _ in range(V + 1)]
temp = list(map(int, input().split()))

# 트리 저장
for i in range(E):
    p, c = temp[2 * i], temp[2 * i + 1]
    # 왼쪽자식칸 비어있으면 왼쪽자식으로 설정
    if tree[p][0] == 0:
        tree[p][0] = c
    # 오른쪽자식으로 설정
    else:
        tree[p][1] = c
    # 자식의부모 설정
    tree[c][2] = p

preorder(1)