def solution(d, budget):
    answer = 0
    for num in sorted(d) :
        if budget - num >=0 :
            answer+=1
            budget = budget - num
    return answer


print(solution([1,3,2,5,4],9))