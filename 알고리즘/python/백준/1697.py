from _collections import deque

def BFS(v):
    visited[v] = 1

    q = deque()
    q.append(v)

    while q:
        start = q.popleft()
        if start == K:
            return
        A = start-1
        B = start+1
        C = start*2

        if 0<=A<=100000 and visited[A] == 0:
            visited[A] = visited[start] + 1
            q.append(A)
        if 0<=B<=100000 and visited[B] == 0:
            visited[B] = visited[start] + 1
            q.append(B)
        if 0<=C<=100000 and visited[C] == 0:
            visited[C] = visited[start] + 1
            q.append(C)

N, K = map(int, input().split())

visited = [0]*100001

BFS(N)

print(visited[K] - 1)