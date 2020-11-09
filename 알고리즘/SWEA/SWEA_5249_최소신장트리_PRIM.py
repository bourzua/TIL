import sys
sys.stdin = open("5249.txt", "r")

import heapq

def MST_PRIM():
    visited = [False]*(V+1)
    heap = []
    # 가중치와 점 오름차순으로
    heapq.heappush(heap, (0, 0))
    ans = 0
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            ans += w
            visited[v] = True
            for weight, idx in adj[v]:
                if not visited[idx]:
                    heapq.heappush(heap,(weight, idx))
    return ans

for T in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for i in range(E):
        st, ed, weight = map(int, input().split())
        adj[st].append((weight, ed))
        adj[ed].append((weight, st))

    print("#{} {}".format(T, MST_PRIM()))