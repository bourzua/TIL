import heapq
import math
def MST_PRIM():
    visited = [False]*N
    heap = []
    heapq.heappush(heap, (0, 0))
    ans = 0
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            ans += w
            visited[v] = 1
            for weight, idx in adj[v]:
                if not visited[idx]:
                    heapq.heappush(heap, (weight, idx))
    return ans

N = int(input())
arr = []
for i in range(N):
    a, b = map(float, input().split())
    arr.append((a, b))
dists = []
for i in range(N):
    for j in range(i+1, N):
        dist = math.sqrt(((arr[i][0] - arr[j][0])**2) + ((arr[i][1] - arr[j][1])**2))
        dists.append((i, j, dist))
adj =[[] for _ in range(N)]
while dists:
    st, ed, weight = dists.pop(0)
    adj[st].append((weight, ed))
    adj[ed].append((weight, st))
print(format(MST_PRIM(), ".2f"))