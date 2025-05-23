# 1 - 0 / 0 - x

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y,graph,visited):
    count = 1
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                count+= dfs(nx,ny,graph,visited)
    return count

count_arr = []
n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            count_arr.append(dfs(i,j,graph, visited))

print(len(count_arr))
for data in sorted(count_arr):
    print(data)