# 문자열 s 가 입력 첫 글자 x
# x 가 기준 문자열 - 다른 글자라면 second+=1
# if first == second -> answer.append(str)
from itertools import count


def solution(s):
    first = 0
    second = 0
    answer = 0
    word = s[0]
    i = 0
    while i < len(s):
        if word == s[i]:
            first+=1
        elif not s[i] == word:
            second+=1

        if first == second :
            answer+=1
            first = 0
            second = 0
            if i <len(s)-1:
                word = s[i+1]
        if len(s)-1 ==i and not first == second:
            answer+=1
            break
        i += 1
    return answer

print(solution("abracadabra"))

