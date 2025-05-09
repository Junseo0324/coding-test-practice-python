def solution(s):
    arr = s.split(' ')
    answer = []
    for str in arr:
        word = ''
        for i in range(len(str)):
            if i%2 ==0 :
                word += str[i].upper()
            else : word +=str[i].lower()
        answer.append(word)
    return " ".join(answer)

print(solution("try hello world"))