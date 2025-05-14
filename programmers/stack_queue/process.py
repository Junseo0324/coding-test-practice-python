# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
from collections import deque


def solution(priorities, location):
    queue = deque(enumerate(priorities))
    answer = 0

    while True:
        current = queue.popleft()
        if  any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer+=1
            if current[0] == location:
                return answer

print(solution([2, 1, 3, 2],2))