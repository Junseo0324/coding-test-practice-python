from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y,graph):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y]+1
                    queue.append((nx,ny))
    return graph[n-1][m-1]


n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]

print(bfs(0,0,graph))


