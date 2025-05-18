from itertools import permutations

def solution(numbers):

    answer = 0
    combination_arr = []
    for i in range(1,len(numbers)+1):
        for data in permutations(numbers,i):
            combination_arr.append(''.join(data))

    for num in set(map(int,combination_arr)):
        if isPrime(num):
            answer+=1

    return answer

def isPrime(number):
    if number <=1:
        return False
    for i in range(2,number):
        if number % i ==0:
            return False
    return True

print(solution("17"))