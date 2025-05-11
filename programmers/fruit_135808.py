# (최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수)
# 사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score
# 3,3,2,2 / 1,1,1
# reverse -> 큰 순으로 정렬 후 m씩 자름
#   if 끝났는데 사이즈가 m이 안될 경우 버린다.
#   사이즈 정렬 후 answer += min(list) x m
def solution(k, m, score):
    answer = 0
    chunked_score = chunked(sorted(score, reverse=True),m)
    for fruit_list in chunked_score:
        if len(fruit_list) == m :
            answer += min(fruit_list) * m
    return answer

def chunked(seq, size):
    return [seq[i:i+size] for i in range(0, len(seq), size)]


print(solution(3,4,[1,2,3,1,2,3,1]))