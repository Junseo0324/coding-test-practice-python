from collections import deque


def dfs(node,visited,graph):
    visited[node] = True
    print(node,end=" ")
    for neighbor in sorted(graph[node]):
        if not visited[neighbor]:
            dfs(neighbor,visited,graph)

def bfs(start,graph):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        curr = queue.popleft()
        print(curr,end=" ")
        for neighbor in sorted(graph[curr]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] *(m+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(v,visited, graph)

print()
bfs(v,graph)



