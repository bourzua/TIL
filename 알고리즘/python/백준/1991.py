# 트리를 리스트로 구현 => 실패
#
# N = int(input())
# tree = [0]*100
#
# for i in range(N):
#     a, b, c = input().split()
#
#     if a not in tree:
#         idx = -1
#     else:
#         idx = tree.index(a)
#
#
#     if idx == -1:
#         tree[1] = a
#         if b != '.':
#             tree[2] = b
#         if b != '.':
#             tree[3] = c
#
#     else:
#         if b != '.':
#             tree[idx*2] = b
#         if c != '.':
#             tree[idx*2 + 1] = c
#
# def preOrder(v):
#     print(tree[v], end="")
#     if tree[v*2] != 0:
#         preOrder(v*2)
#     if tree[v*2 + 1] != 0:
#         preOrder(v*2 + 1)
#
# def inOrder(v):
#     if tree[v*2] != 0:
#         inOrder(v*2)
#     print(tree[v], end="")
#     if tree[v*2 + 1] != 0:
#         inOrder(v*2 + 1)
#
# def postOrder(v):
#     if tree[v * 2] != 0:
#         postOrder(v * 2)
#     if tree[v*2 + 1] != 0:
#         postOrder(v*2 + 1)
#     print(tree[v], end="")
#
# preOrder(1)
# print()
# inOrder(1)
# print()
# postOrder(1)


import sys
sys.setrecursionlimit(10**6)

def preorder(node):
    if node == '.':
        return
    print(node, end="")
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end="")

N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')