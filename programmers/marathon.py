# 한 명을 제외하고 모두 완주
# participant -> 참여 선수 명단
# completion -> 완주한 선수
# 완주하지 못한 선수 return


#def solution(participant, completion):
#    answer = participant.copy()
#    ex_completion = completion.copy()
#    for person in participant:
#        if person in ex_completion:
#            answer.remove(person)
#            ex_completion.remove(person)
#
#    return answer

from collections import Counter

def solution(participant, completion):
    part_count = Counter(participant)
    comp_count = Counter(completion)
    answer = part_count - comp_count

    return list(answer.keys())[0]


print(solution(["mislav", "stanko", "mislav", "ana"],
               ["stanko", "ana", "mislav"]))
