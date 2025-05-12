def solution(lottos, win_nums):
    zero_count = 0
    match_count =0

    for lotto in sorted(lottos,reverse=True):
        if lotto == 0:
            zero_count +=1
        else:
            if lotto in win_nums:
                match_count +=1
    answer = []
    if match_count ==6:
        answer.append(1)
    elif match_count == 5:
        answer.append(2)
    elif match_count ==4:
        answer.append(3)
    elif match_count == 3:
        answer.append(4)
    elif match_count == 2:
        answer.append(5)
    else:
        answer.append(6)

    max_count = zero_count + match_count
    if max_count ==6:
        answer.append(1)
    elif max_count == 5:
        answer.append(2)
    elif max_count ==4:
        answer.append(3)
    elif max_count == 3:
        answer.append(4)
    elif max_count == 2:
        answer.append(5)
    else:
        answer.append(6)


    return sorted(answer)

print(solution([45, 4, 35, 20, 3, 9]	,[20, 9, 3, 45, 4, 35]	))