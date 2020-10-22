def BFS(a):
    queue = []
    # 시작점을 넣는다.
    queue.append(a)
    visited[a] = 1

    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr, end=" ")

        for i in adj_list[curr]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

V, E = map(int, input().split())

adj_list = [[] for _ in range(V+1)]

# [[],[],[],[],[]]

for i in range(E):
    st, ed = map(int, input().split())
    adj_list[st].append(ed)
    adj_list[ed].append(st)

visited = [0]*(V+1)