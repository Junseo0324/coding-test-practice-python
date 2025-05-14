# 초 단위로 기록된 주식가격이 담긴 배열 prices
# 가격이 떨어지지 않은 기간은 몇초인지 return


def solution(prices):
    answer = []
    stack = []
    for i in range(len(prices)-1) :
        if len(stack) == 0:
            stack.append(prices[i])
            answer.append(1)
        else:
            for j in range(len(stack)) :
                if stack[j] <= prices[i]:
                    answer[j] +=1
            stack.append(prices[i])
            answer.append(1)
    answer.append(0)
    return answer

def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top

    return answer



print(solution([5,4,3,2,1]))