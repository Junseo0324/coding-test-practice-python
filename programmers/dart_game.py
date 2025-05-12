# S(single) - 1제곱 / D(Double) - 2 / Triple(T) - 3
# 옵션 - 스타상(*) -해당 점수 & 바로 직전 점수 2배,
# 아차상(#) - 해당 점수 마이너스,
# 스타상 - 첫 번째 기회에도 나올 수 있다. 첫번째만 점수 2배
# 스타상의 효과는 다른 스타상의 효과와 중첩 가능 이경우 4배가 된다.
# 스타상의 효과는 아차상과 중첩 가능 -> 중첩된 아차상의 점수는 -2배

#-------------
# for 문의 경우 10을 처리하는 방식에서 불편함을 느낌(?)

def solution(dartResult):
    score = []
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit():
            if dartResult[i] == '1' and i +1 <len(dartResult) and dartResult[i+1] =='0':
                num = 10
                i+=1
            else:
                num = int(dartResult[i])
            score.append(num)
        elif dartResult[i] in ['S','D','T'] :
            if dartResult[i] == 'S':
                score[-1] **= 1
            elif dartResult[i] == 'D':
                score[-1] **= 2
            else :
                score[-1] **= 3
        elif dartResult[i] == '*':
            score[-1] *=2
            if len(score) >=2:
                score[-2] *=2
        elif dartResult[i] == '#':
            score[-1] *= -1
        i+=1
    return sum(score)
    # for dart in dartResult:
    #     if dart.isdigit():
    #         score.append(int(dart))
    #     elif dart in ['S','D','T']:
    #         if dart == 'S':
    #             score[len(score)-1] = score[len(score)-1] ** 1
    #         elif dart == 'D':
    #             score[len(score)-1] = score[len(score)-1] ** 2
    #         else :
    #             score[len(score)-1] = score[len(score)-1] ** 3
    #     else :
    #         if dart == '*' :
    #             last = len(score)-1
    #             if last ==1:
    #                 score[last] = score[last] *2
    #             else:
    #                 score[last] = score[last] * 2
    #                 score[len(score) - 2] = score[len(score) - 2] * 2
    #         elif dart == '#':
    #             score[len(score)-1] = - score[len(score)-1]
    # print(score)
    # return sum(score)



print(solution("1D2S#10S"))



