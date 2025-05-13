# 각 종류별 1개 의상만 착용 가능
# clothes [의상 이름, 종류] 로 구성
# 종류+1,종류+1 x2 -1

# Counter 를 사용하는 방법도 존재.
# from collections import Counter
def solution(clothes):
    #
    # cnt = Counter([v for k,v in clothes])
    # print(cnt)
    hash = {}
    for cloth in clothes:
        if cloth[1] in hash.keys():
            hash[cloth[1]] +=1
        else:
            hash[cloth[1]] = 2
    answer = 1
    for v in hash.values():
        answer *= v
    return answer -1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	))