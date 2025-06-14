from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int,input())) for _ in range(n)]
    dist = [[float('inf')]*n for _ in range(n)]
    dist[0][0] = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    queue = deque()
    queue.append((0,0))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]

            if 0<=nx<n and 0<=ny<n:
                cost = dist[x][y] + graph[nx][ny]
                if cost< dist[nx][ny]:
                    dist[nx][ny] = cost
                    queue.append((nx,ny))


    print(f"#{test_case} {dist[n-1][n-1]}")
