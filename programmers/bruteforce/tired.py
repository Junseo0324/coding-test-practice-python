# 하루에 한번씩 탐험할 수 있는 던전이 여러 개 존재. 이 던전을 최대한 많이 탐험
#현재 피로도 k & 던전별 (최소 필요 피로도, 소모 필요도)
import copy
# 각 던전마다 탐험을 시작하기 위해 필요한 최소 필요 피로도 ,
# 던점 끝 -> 소모되는 소모 필요도 존재.

# 유저가 탐험할 수 있는 최대 던전 수 return
# 1<k<5000 / dungeonu -> 1 ~ 8

# 8! = 1x2x3x4x5x6x7x8 = 720 x 7 = 5040 x8 = 40320
from itertools import permutations
import copy

def solution(k, dungeons):
    answer = -1
    for dungeon in permutations(dungeons):
        count = 0
        curr = copy.deepcopy(k)
        for tiredList in dungeon :
            if curr >= tiredList[0] :
                curr = curr-tiredList[1]
                count+=1
            else:
                break
        answer = max(answer,count)

    return answer


print(solution(80,[[80,20],[50,40],[30,10]]))


