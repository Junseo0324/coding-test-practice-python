def solution(food):
    answer = ''
    for idx,num in enumerate(food):
        answer+= (num//2)*str(idx)

    return answer + '0' + answer[::-1]
    
print(solution([1,3,4,6]))
