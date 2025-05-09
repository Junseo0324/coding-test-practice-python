import math

def solution(n):
    num = math.sqrt(n)
    if num.is_integer():
        return (num+1)*(num+1)
    return -1

print(solution(121))