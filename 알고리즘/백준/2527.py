# 한 조건씩 걸러진다는 걸 생각해야됨!

for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int,input().split())

    if p1<x2 or q1<y2 or y1>q2 or x1>p2:
        print("d")
    elif (x1==p2 and y1==q2) or (p1==x2 and y1==q2) or (p1==x2 and q1==y2) or (x1==p2 and q1==y2):
        print("c")
    elif x2==p1 or p2==x1 or y2==q1 or q2==y1:
        print("b")
    else:
        print("a")