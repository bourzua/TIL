import sys
N = int(sys.stdin.readline())

users = []

for i in range(N):
     a, b = sys.stdin.readline().split()
     a = int(a)
     users.append([a, b])

users.sort(key= lambda x: x[0])

for i in range(N):
    print(users[i][0], users[i][1])