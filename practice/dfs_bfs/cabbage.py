
import sys
sys.setrecursionlimit(10**6)

T = int(input())

for test_case in range(1,T+1):
    m,n,k = map(int,input().split())

    graph = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1

    def dfs(x,y,visited,graph):
        visited[y][x] = True

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<m and 0<=ny<n:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    dfs(nx,ny,visited, graph)

    answer = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] ==1:
                dfs(j,i,visited, graph)
                answer+=1
    print(answer)