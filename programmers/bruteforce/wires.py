'''
n 개의 송전탑이 전선을 통해 하나의 트리 형태로 연결
이 전선들 중 하나를 끊어 현재의 전력망 네트워크를 2개로 분할
두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 함.
n = 송전탑 개수 /  전선 정보 = wires

가장 비슷할 때 두 전력망이 가지고 있는 송전탑 개수의 차이(절댓값)를 return
wires 는 길이가 n-1 / [v1,v2] -> 1 <= v1 < v2 <= n

wires -> graph 형태로 나타낸 후
for wires 문을 돌림. 그 wires에 해당하는 graph 데이터 삭제 후 dfs 수행해서 2개의 count 세기.
그 count 값을 빼서 answer = min(count,answer) 처리.


dfs 이용(?)
for 문 n번
    count를 세서 그 count 끼리의 차이값 저장
for문이 끝날 때 min(count,answer)해서
최솟값을 return
'''


def dfs(node, graph, visited):
    visited[node] = True
    count = 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(neighbor, graph, visited)
    return count

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]
    # graph 생성
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        visited = [False] * (n + 1)
        count = dfs(a, graph, visited)
        diff = abs((n - count) - count)
        answer = min(answer, diff)

        graph[a].append(b)
        graph[b].append(a)

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
