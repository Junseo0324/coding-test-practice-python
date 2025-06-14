rotate = [(0,1),(1,0),(0,-1),(-1,0)]

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    x, y = (0, 0)
    r_idx = 0
    for i in range(1,n*n+1):
        graph[x][y] = i
        next_x,next_y = rotate[r_idx % 4]
        if (0<= next_x+x < n  and 0<= next_y+y<n) and graph[next_x+x][next_y+y] == 0:
            x += next_x
            y += next_y
        else:
            r_idx+=1
            next_x,next_y = rotate[r_idx % 4]
            x +=next_x
            y +=next_y

    print(f"#{test_case}")
    for i in range(n):
        print(*graph[i])