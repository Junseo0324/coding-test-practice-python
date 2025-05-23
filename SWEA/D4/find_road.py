def dfs(node,visited,graph):
    visited[node] = True
    if node == 99:
        return 1
    for i in graph[node]:
        if not visited[i]:
            if dfs(i,visited,graph):
                return 1
    return 0

for test_case in range(1, 11):
    n,road = map(int,input().split())
    graph = [[] for _ in range(100)]
    data = list(map(int,input().split()))
    for i in range(0,len(data),2):
        graph[data[i]].append(data[i+1])
    visited =[False] * 100
    answer = dfs(0,visited,graph)

    print(f"#{test_case} {answer}")
