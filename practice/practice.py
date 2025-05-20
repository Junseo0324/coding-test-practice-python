from SWEA.D3.max_money import visited


# def dfs(node,visited,graph):
#     visited[node] = True
#     print(node,end=' ')
#
#     for i in graph[node]:
#         if not visited[i]:
#             dfs(i,visited,graph)
#
# def solution():
#     graph = {
#         0: [1, 2],
#         1: [0, 3],
#         2: [0, 4],
#         3: [1],
#         4: [2]
#     }
#     visited = [False] * 5
#     dfs(0, visited, graph)

# solution()

def dfs(x,y):
    visited[x][y] = True

    for i in range(4):
        nx = x+dx[i]
        ny = y +dy[i]

        if 0<=nx < n and 0 <= ny <m :
            if not visited[nx][ny] and board[nx][ny] == 1:
                dfs(nx,ny)


def solution():
    dx= [1,0,-1,0]
    dy = [0,1,0,-1]

    