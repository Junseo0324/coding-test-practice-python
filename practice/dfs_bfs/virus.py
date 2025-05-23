
n = int(input())
m = int(input())
visited = [False] * (n + 1)

def dfs(v,visited):
    visited[v] = True
    count = 1
    for i in graph[v]:
        if not visited[i]:
            count +=dfs(i,visited)
    return count

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


print(dfs(1,visited)-1)

