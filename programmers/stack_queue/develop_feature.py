# 각 기능은 100%일 때 반영 가능
# 뒤에 있는 기능이 앞보다 먼저 가능
#   but 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 같이 배포된다.
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses
# 각 작업의 개발 속도가 적힌 speeds
# 각 배포마다 몇 개의 기능이 배포되는지 return
from queue import Queue


def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        if count > 0:
            answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
