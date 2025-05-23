# dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*n for _ in range(n)]

    dp[0][0] = arr[0][0]

    for j in range(1,n):
        dp[0][j] = dp[0][j-1]+arr[0][j]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + arr[i][0]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]

    print(f"#{test_case} {dp[n-1][n-1]}")
