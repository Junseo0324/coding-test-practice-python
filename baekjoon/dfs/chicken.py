from itertools import combinations

n,m = map(int,input().split())
#1 - 집 2 - 치킨
graph = [list(map(int,input().split())) for _ in range(n)]
home_arr = []
chicken_arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home_arr.append((i,j))

        if graph[i][j] == 2:
            chicken_arr.append((i,j))

min_length = float('inf')

for combination in combinations(chicken_arr,m):
    total = 0
    for x,y in home_arr:
        dist = float('inf')
        for case_x,case_y in combination:
            dist = min(dist,abs(x-case_x) + abs(y - case_y))
        total +=dist
    min_length = min(min_length,total)


print(min_length)