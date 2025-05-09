def solution(name, yearning, photo):
    answer = []
    score_dict = dict(zip(name,yearning))
    for person_list in photo:
        score = 0
        for person in person_list:
            score += score_dict.get(person,0)
        answer.append(score)
    return answer


print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
