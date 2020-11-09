# DFS로 했다가 BFS로 변경
# DFS가 안되는 이유는 굿노트에

def BFS(v, count):
    global MIN
    visited[v] = 1
    q = [(v, count)]
    while q:
        curr_v, curr_count = q.pop(0)
        if curr_v == G:
            if curr_count < MIN:
                MIN = curr_count
            return
        if curr_count > MIN:
            continue
        if curr_v + U <= F and visited[curr_v + U] == 0:
            visited[curr_v + U] = 1
            q.append((curr_v + U, curr_count +1))
        if curr_v - D >= 1 and visited[curr_v - D] == 0:
            visited[curr_v - D] = 1
            q.append((curr_v - D, curr_count + 1))


F, S, G, U, D = map(int, input().split())
visited = [0]*(F+1)
MIN = 0xfffffff
BFS(S, 0)
if MIN == 0xfffffff:
    print('use the stairs')
else:
    print(MIN)