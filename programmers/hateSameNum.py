def solution(arr):
    stack = []
    for num in arr :
        if len(stack) !=0 :
            if stack[-1] != num :
                stack.append(num)
        else :
            stack.append(num)
    return stack

print(solution([1,1,3,3,0,1,1]))