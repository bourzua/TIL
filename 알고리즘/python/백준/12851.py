from collections import deque

N, K = map(int, input().split())

# N이 K보다 크면 -1로 내려갈수밖에 없어서 N-K초
if N >= K:
    print(N - K)
    print(1)

else:
    visited = [False] * 100001
    ans = 100001  # 최소 초 초기값
    amount = 0  # 최소 초 경우의수
    q = deque()
    q.append((K, 0))  # 현위치, 현위치 초수
    while q:
        pos, cnt = q.popleft()
        visited[pos] = True  # 현위치 방문표시

        # 현 위치보다 초수 넘어가면 건너뜀
        if cnt > ans:
            continue

        # 위치가 N에 도달하면
        if pos == N:
            # cnt가 ans(최소초수)보다 작으면 갱신, amount도 1개로 리셋
            if cnt < ans:
                ans = cnt
                amount = 1
            elif cnt == ans:  # 최소초수랑 같다면 경우의수 1증가
                amount += 1

        else:
            # 짝수일때 방문도 안했다면 q에 pos//2 추가
            if not pos % 2 and not visited[pos % 2]:
                q.append((pos // 2, cnt + 1))
            # 1뺀게 범위에서 벗어나지 않고 방문 안했다면 q에 pos-1추가
            if 0 <= pos - 1 and not visited[pos - 1]:
                q.append((pos - 1, cnt + 1))
            # 1더한게 범위에서 벗어나지 않고 방문 안했다면 q에 pos+1추가
            if pos + 1 <= 100000 and not visited[pos + 1]:
                q.append((pos + 1, cnt + 1))

    print(ans)
    print(amount)