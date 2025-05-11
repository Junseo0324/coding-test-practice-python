from itertools import combinations


def solution(nums):
    answer = 0
    for arr in combinations(nums,3):
        if isPrime(sum(arr)):
            answer +=1

    return answer


def isPrime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

print(solution([1,2,7,6,4]))