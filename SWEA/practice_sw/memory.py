T = int(input())
for test_case in range(1, T + 1):
    data = list(map(int,input()))

    answer = 0
    curr = 0
    for d in data:
        if d != curr:
            answer+=1
            curr = d

    print(f"#{test_case} {answer}")

