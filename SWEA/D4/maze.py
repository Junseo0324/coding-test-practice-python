'''
16 x 16 미로
0 = 길 / 1= 벽
0,0 기준 시작점 2 도착점 3
도달 가능 1 / 안됨 0

'''
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y,visited,graph):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx< 16 and 0<=ny<16:
                if not visited[nx][ny] and graph[nx][ny] in (0,3) :
                    if graph[nx][ny] == 3:
                        return 1
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return 0


for test_case in range(1,11):
    test_number = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    start_x = start_y = -1
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                start_x = i
                start_y = j
                break
        if start_x !=-1:
            break

    answer = bfs(start_x,start_y,visited,graph)

    print(f"#{test_case} {answer}")


