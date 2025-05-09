def solution(phone_number):
    last = phone_number[-4:]
    count = len(phone_number) - 4
    return '*' * count + last

print(solution("023234444"))