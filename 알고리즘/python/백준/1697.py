# 가장 무식한 방법: +1을 10만 번
# *2를 계속하면 언젠가 20만이 넘을 수는 있음
# but 20만에서 10만으로 오려면 10만 번 와야하기 때문에 가장 무식한 방법의 횟수를 넘을 수가 있음
# => 갈 수 있는 자리는 20만이 최대
from collections import deque

n, m = map(int, input().split())
MAX = 200000
visited = [-1]*(MAX + 1)

q = deque()
q.append(n)
visited[n] = 0

while q:
    curr = q.popleft()
    if curr == m:
        break
    for nxt in [curr + 1, curr - 1, curr * 2]:
        if 0<=nxt<=MAX and visited[nxt] == -1:
            visited[nxt] = visited[curr] + 1
            q.append(nxt)
print(visited[m])