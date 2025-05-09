def solution(s):
    dic = {}
    for str in s:
        if str in dic :
            dic[str.lower()] +=1
        else :
            dic[str.lower()] = 1
    return dic.get("p",0) == dic.get("y",0)


def solution2(s):
    s = s.lower()
    return s.count('p') == s.count('y')

print(solution("Pyy"))
print(solution2("PppPoodafYyy"))