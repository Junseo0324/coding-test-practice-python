from itertools import combinations

def solution(numbers):
    answer = []
    for i in combinations(numbers,2) :
        answer.append(sum(i))
    
    return sorted(set(answer))


print(solution([2,1,3,4,1]))