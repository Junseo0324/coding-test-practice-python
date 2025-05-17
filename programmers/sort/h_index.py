# H-index
# n 편 논문 중 h 번 이상 인용된 논문이 h편 이상
# 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 h-index
# [3,0,6,1,5] =citations
# 5개 중 3편은 3번 이상 인용. h-index = 3
from itertools import count


def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for c in citations:
        if c > answer:
            answer+=1

    return answer


print(solution([3,0,6,1,5]))

