from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    road_arr = [list(map(int, input().strip())) for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist[x][y] + road_arr[nx][ny]
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    queue.append((nx, ny))

    print(f"#{test_case} {dist[n - 1][n - 1]}")
