T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int,input().split())

    graph = [list(map(int,input().split())) for _ in range(n)]

    answer = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            for k in range(m):
                for l in range(m):
                    total += graph[i+k][j+l]
            answer = max(total,answer)

    print(f"#{test_case} {answer}")

