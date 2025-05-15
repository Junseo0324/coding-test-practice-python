for test_case in range(1, 11):
    dump = int(input())
    box_arr = list(map(int, input().split()))
    i = 1
    while i <= dump:
        box_arr[box_arr.index(max(box_arr))] -= 1
        box_arr[box_arr.index(min(box_arr))] += 1
        i += 1

    print("#"+str(test_case)+" "+str(max(box_arr) - min(box_arr)))

