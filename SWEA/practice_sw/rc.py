T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    speed = 0
    answer = 0
    for i in range(n):
        data = input().strip()

        if len(data) == 1:
            answer+=speed
        else:
            a,b = map(int,data.split())
            if a == 1:
                speed += b
                answer += speed
            elif a ==2:
                if speed-b <0:
                    speed =0
                else:
                    speed -=b
                answer +=speed
    print(f"#{test_case} {answer}")