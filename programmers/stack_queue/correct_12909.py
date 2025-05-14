def solution(s):
    stack = []
    for word in s:
        if not len(stack) == 0:
            if word =='(' :
                stack.append(word)
            else: # ) 일 경우
                if stack[-1] == '(' :
                    stack.pop()
                else:
                    return False
        else:
            if word == ')':
                return False
            else:
                stack.append(word)

    if len(stack) >0:
        return False
    return True


print(solution("(()("	))