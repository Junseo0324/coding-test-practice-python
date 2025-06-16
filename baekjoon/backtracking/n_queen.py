# n x n 체스판 존재

n = int(input())
count = 0
col = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)


def dfs(row):
    global count
    if row == n :
        count+=1
        return

    for i in range(n):
        if not col[i] and not diag1[i+row] and not diag2[i - row + n - 1]:
            col[i] = diag1[i+row] = diag2[i - row + n - 1] = True
            dfs(row+1)
            col[i] = diag1[i+row] = diag2[i - row + n - 1] = False

dfs(0)
print(count)
