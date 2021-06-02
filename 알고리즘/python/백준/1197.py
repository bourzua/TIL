import heapq

def MST_PRIM():
    visited = [False]*(V+1)
    heap = []
    heapq.heappush(heap, (0, 1))
    ans = 0
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            ans += w
            visited[v] = 1
            for weight, v in adj[v]:
                if not visited[v]:
                    heapq.heappush(heap, (weight, v))
    return ans

V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    st, ed, weight = map(int, input().split())
    adj[st].append((weight, ed))
    adj[ed].append((weight, st))
print(MST_PRIM())