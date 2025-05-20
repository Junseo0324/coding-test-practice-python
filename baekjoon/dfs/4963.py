import sys
sys.setrecursionlimit(10**6)

def dfs(x,y,visited,graph):
    visited[y][x] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y+ dy[i]

        if 0<=nx< w and 0 <= ny < h:
            if not visited[ny][nx] and graph[ny][nx]==1:
                dfs(nx,ny,visited,graph)


dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))

    visited = [[False]*w for _ in range(h)]
    answer = 0
    for i in range(w):
        for j in range(h):
            if not visited[j][i] and graph[j][i] == 1:
                dfs(i,j,visited, graph)
                answer+=1
    print(answer)