# 문자열 작성할 수 없을 경우 -1
# 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열 배열 keymap
# 입력하려는 문자열 target
# 몇 번씩 눌러야 하는지 순서대로 배열에 담아 return
#

def solution(keymap, targets):
    answer = []
    for target in targets:
        count = 0
        for word in target:
            min_idx = 101
            isCheck = False
            for key in keymap:
                if word in key:
                    min_idx = min(min_idx,key.index(word)+1)
                    isCheck = True
            if isCheck :
                count +=min_idx
            else:
                count+=100000
        if count >=100000 :
            answer.append(-1)
        else :
            answer.append(count)
    return answer



print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))