# import sys
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#     N = int(sys.stdin.readline())
#     # 노드별로 부모가 누군지 알려주는 그래프
#     parent = [0]*(N+1)
#     ans = 0
#
#     # 노드별로 부모가 누군지 알려주는 그래프 만들기
#     for _ in range(N-1):
#         a, b = map(int, sys.stdin.readline().split())
#         parent[b] = a
#
#     node1, node2 = map(int, sys.stdin.readline().split())
#     # 부모 목록 다 구하기
#     parent1 = [node1]
#     parent2 = [node2]
#     while True:
#         # 부모 없으면 나와
#         if not parent[node1]:
#             break
#         # 부모 찾고 넣고 걔를 자식으로 만들기
#         node1 = parent[node1]
#         parent1.append(node1)
#     while True:
#         if not parent[node2]:
#             break
#         node2 = parent[node2]
#         parent2.append(node2)
#     # 뭐 하나 같은거 나오면 맨처음에 나온게 가장 가까운 부모!
#     for i in parent1:
#         if i in parent2:
#             ans = i
#             break
#
#     print(ans)

import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    # 노드별로 부모가 누군지 알려주는 그래프
    parent = [0]*(N+1)
    ans = 0

    # 노드별로 부모가 누군지 알려주는 그래프 만들기
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        parent[b] = a

    node1, node2 = map(int, sys.stdin.readline().split())
    # 부모 목록 다 구하기
    parent1 = [node1]
    # parent2 = [node2]
    while True:
        # 부모 없으면 나와
        if not parent[node1]:
            break
        # 부모 찾고 넣고 걔를 자식으로 만들기
        node1 = parent[node1]
        parent1.append(node1)
    while True:
        if not parent[node2]:
            break
        node2 = parent[node2]
        if node2 in parent1:
            ans = node2
            break
        # parent2.append(node2)
    # 뭐 하나 같은거 나오면 맨처음에 나온게 가장 가까운 부모!
    # for i in parent1:
    #     if i in parent2:
    #         ans = i
    #         break

    print(ans)