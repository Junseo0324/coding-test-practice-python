# 모음 'A','E','I','O','U' 만을 이용해 만들 수 있는 길이 5 이하의 모든 단어 수록
# 첫 번재 단어 -> A
# 그 다음 AA
# 마지막 단어 UUUUU

# word 가 주어질 때 이 단어가 사전에서 몇 번째 단어인지 return
# 경우의 수 = 5x5x5x5x5 = 625 x 5  = 3125
# 5글자 -> index 1  4+(i) = 6
# 4글자 -> index 1 3+ix5 + (i+1) =10
# 3글자 -> 1x5^4 (625)+ 2x5^3 (2
# 50) + 3x5^2 (75) +
# EA -> 626
# EEA -> 625 + 125 + 1
# ix5^4 + i x 5^3
# i -> 625x3 = 1875


def solution(word):
    word_arr = ["A","E","I","O","U",""]
    answer = 0
    word_list = []
    for i in word_arr:
        for j in word_arr:
            for k in word_arr:
                for l in word_arr:
                    for m in word_arr:
                        w = i + j +k+l+m
                        if w not in word_list:
                            word_list.append(w)

    word_list.sort()
    answer = word_list.index(word)
    return answer

print(solution("I"))

# answer = 0
# isFind = False
# def solution(word):
#     alpha = ['A','E','I','O','U']
#
#     def word_dfs(s,start):
#         for i in alpha:
#             if not isFind: break
#
#             curr = s + i
#             answer+=1
#
#             if curr == start:
#                 isFind = True
#             elif not len(curr) == 5:
#                 word_dfs(curr,word)
#



