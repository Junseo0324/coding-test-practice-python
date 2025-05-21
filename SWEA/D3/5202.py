T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    schedule = [tuple(map(int,input().split())) for _ in range(n)]
    schedule.sort(key=lambda x:x[1])
    print(schedule)
    answer = 0
    end_time = 0

    for start, end in schedule:
        if start >= end_time:
            answer+=1
            end_time = end

    print(f"#{test_case} {answer}")