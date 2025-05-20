# r = 세로 / c = 가로
# 보드이 각 칸에는 대문자 알파벳 존재
# 좌측 상단 1-1에 말이 놓여있음 (2차원?)
# 1 <= R,C <=20
def dfs(node,visited,graph):
    visited[node] = True




r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
dx =[1,0,-1,0]
dy =[0,1,0,-1]


print(r,c)
print(graph)