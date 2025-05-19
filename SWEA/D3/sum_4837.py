from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    n,k = map(int,input().split())
    answer = 0
    for data in combinations(range(1,13),n):
        if sum(data) == k:
            answer+=1

    print(f"#{test_case} {answer}")