for _ in range(10):
    test_case = int(input())
    arr = []
    max_row = 0
    max_col = 0
    for i in range(100):
        row_arr = list(map(int, input().split()))
        max_row = max(max_row,sum(row_arr))
        arr.append(row_arr)

    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += arr[j][i]
        max_col = max(max_col,col_sum)

    diagonal_sum = 0
    diagonal_minus_sum = 0

    # 대각선 arr[i][i]
    for i in range(100):
        diagonal_sum += arr[i][i]
        diagonal_minus_sum += arr[i][-i]


    print("#"+str(test_case)+" "+str(max(max_row,max_col,diagonal_sum,diagonal_minus_sum)))
