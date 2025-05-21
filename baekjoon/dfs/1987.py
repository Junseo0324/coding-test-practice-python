# r = 세로 / c = 가로
# 보드이 각 칸에는 대문자 알파벳 존재
# 좌측 상단 1-1에 말이 놓여있음 (2차원?)
# 1 <= R,C <=20
# 좌측 상단(0,0)에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지
# 변수 answer = 지난 칸
# visited 를 어떻게 설정할 것인지..

visited = set()
def dfs(x, y, path):
    global answer
    answer = max(answer,len(path))


    key = (x,y,tuple(sorted(path)))
    if key in visited:
        return
    visited.add(key)


    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0 <= nx < r and 0 <= ny < c:
            char = graph[nx][ny]
            if char not in path:
                path.add(char)
                dfs(nx,ny,path)
                path.remove(char)



r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0

dfs(0,0,set(graph[0][0]))

print(answer)
