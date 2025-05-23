from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y,visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    dist = [[0] * n for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif graph[nx][ny] == 3:
                    return dist[x][y]

    return 0


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n  for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j]==2:
                answer = bfs(i,j,visited)

    print(f"#{test_case} {answer}")