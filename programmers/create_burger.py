# 햄버거 포장
# 빵 - 야채 - 고기 - 빵 순으로만. 1231
#

def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            for _ in range(4):
                stack.pop()
            answer+=1
    return answer




print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]	))