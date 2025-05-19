T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    answer = []
    size = len(arr)-1
    for i in range(len(arr)//2):
        if len(answer) == 10:
            break
        answer.append(arr[size - i])
        answer.append(arr[i])

    print(f"#{test_case} {' '.join(map(str,answer))}")
