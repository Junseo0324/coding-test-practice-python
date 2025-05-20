def dfs(node, visited, graph):
    visited[node] = True
    global answer
    answer += 1

    for i in graph[node]:
        if not visited[i]:
            dfs(i, visited, graph)


n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for i in range(m):
    start,end = map(int,input().split())
    arr[start].append(end)
    arr[end].append(start)
print(arr)
visited = [False] *(n+1)
answer = 0
dfs(1,visited,arr)

print(answer-1)


