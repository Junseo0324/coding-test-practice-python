from itertools import permutations

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    e = [list(map(int, input().split())) for _ in range(n)]
    total = float('inf')
    for road in permutations(range(1, n)):
        path = [0] + list(road)
        battery = 0
        for i in range(n - 1):
            battery += e[path[i]][path[i + 1]]
        battery += e[path[-1]][path[0]]

        total = min(total, battery)

    print(f"#{test_case} {total}")