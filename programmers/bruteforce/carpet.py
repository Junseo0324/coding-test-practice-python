# 10 , 2 -> [4,3]
# 8, 1 -> [3,3]
# 24,24 -> 48 -> 3x16 4x12 6x8

# brown + yellow 일 때 나올 수 있는 곱하기 면적 경우의 수를 다 구하기.
# 3x16 경우 (3-2)x(16-2) = 14 !=24 / 2 x 10 != 20 / 4 x 6 = 24 -> 답은 6x8
# 카펫의 가로 길이 >= 세로길이


def solution(brown, yellow):
    answer = []
    carpet = brown + yellow #면적
    for i in range(3,carpet):
        if carpet % i == 0:
            x,y = i,carpet // i
            if (x-2) * (y-2) == yellow:
                answer.append(x)
                answer.append(y)
                break

    return sorted(answer,reverse=True)



print(solution(10,2))

