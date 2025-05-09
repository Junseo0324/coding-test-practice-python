def solution(s):
    answer = []
    check = {}
    for i,char in enumerate(s):
        if char in check :
            answer.append(i - check[char])
        else:
            answer.append(-1)
        check[char] = i
    return answer


print(solution("banana"))