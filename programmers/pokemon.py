from itertools import combinations 

def solution(nums):
    answer = 0
    num_set= set(nums)
    if len(num_set) < (len(nums)//2) :
        answer = len(num_set)
    else: answer = (len(nums)//2)

    return answer

print(solution([3,1,2,3]))