n = int(input())
answer = 0

cols = [False] * n
diag1 = [False] * (2 * n)
diag2 = [False] * (2 * n)

def dfs(row):
    global answer
    if row == n:
        answer += 1
        return

    for col in range(n):
        if not cols[col] and not diag1[row + col] and not diag2[row - col + n]:
            cols[col] = diag1[row + col] = diag2[row - col + n] = True
            dfs(row + 1)
            cols[col] = diag1[row + col] = diag2[row - col + n] = False

dfs(0)
print(answer)
