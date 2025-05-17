#  스코빌 지수를 k 이상으로
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 2 <= scoville <= 1,000,000
# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞는다.
# 가진 음식의 스코빌 지수를 담은 배열 scoville & 원하는 스코빌 지수 K
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수

import heapq

# 힙을 사용해서 계산?
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >=2 and scoville[0] < K :
        first_food = heapq.heappop(scoville)
        second_food = heapq.heappop(scoville)
        new = first_food + second_food*2
        heapq.heappush(scoville,new)
        answer+=1
    return answer if scoville[0] >= K else -1


print(solution([1, 2, 3, 9, 10, 12],7))