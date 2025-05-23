'''
등산로는 가장 높은 봉우리에서 시작해야 한다.
높 -> 낮은 지형으로. / 높 같은곳&낮은곳 x
K 깊이만큼 지형 깍는 공사 1회 가능
N * N 크기의 지도가 주어지고, 최대 공사 가능 깊이 K가 주어진다.

이때 만들 수 있는 가장 긴 등산로를 찾아 그 길이를 출력하는 프로그램을 작성하라.
'''
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, graph, length, k_used):
    global max_length
    max_length = max(max_length, length)

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] < graph[x][y]:
                dfs(nx,ny,graph,length+1,k_used)
            elif not k_used and graph[nx][ny] - k < graph[x][y]:
                origin = graph[nx][ny]
                graph[nx][ny] = graph[x][y] -1
                dfs(nx,ny,graph,length+1,True)
                graph[nx][ny] = origin

    visited[x][y] = False


T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    max_height = max(max(row) for row in graph)
    max_length = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == max_height:
                dfs(i,j,graph,1,False)

    print(f"#{test_case} {max_length}")