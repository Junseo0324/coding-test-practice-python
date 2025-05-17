# 0 or 양의 정수가 주어짐. 이어 붙여 만들 수 있는 가장 큰 수
# [6,10,2] => 6210

from itertools import permutations
def solution(numbers):
    numbers = list(map(str,numbers))

    numbers.sort(key= lambda x: x*3,reverse=True)
    return str(int(''.join(numbers)))

print(solution([6,10,2]))