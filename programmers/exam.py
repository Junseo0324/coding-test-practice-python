
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

def solution(answers):

    answer = []
    answer_dic = {}
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]


    for i in range(len(answers)) :
        if arr1[i % len(arr1)] == answers[i]:
            answer_dic[1] = answer_dic.get(1, 0) + 1
        if arr2[i% len(arr2)] == answers[i]:
            answer_dic[2] = answer_dic.get(2,0)+1
        if arr3[i % len(arr3)] == answers[i]:
            answer_dic[3] = answer_dic.get(3,0)+1
    max_score = max(answer_dic.values())
    for person, score in answer_dic.items():
        if score == max_score:
            answer.append(person)
    return sorted(answer)


print(solution([1,3,2,4,2]	))