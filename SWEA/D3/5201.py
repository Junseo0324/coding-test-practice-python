
T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    container = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    answer = 0
    for t in truck:
        for c in container:
            if c <= t:
                answer+=c
                container.remove(c)
                break

    print(f"#{test_case} {answer}")

