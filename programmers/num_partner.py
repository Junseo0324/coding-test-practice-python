from collections import Counter
def solution(X, Y):
    x_count = Counter(X)
    y_count = Counter(Y)

    result = x_count & y_count
    answer = []
    for k,v in result.items():
        for _ in range(v):
            answer.append(k)

    if not answer:
        return '-1'
    if answer[0] == '0':
        return '0'
    return str(''.join(sorted(answer,reverse=True)))

print(solution("5525","1255"))
