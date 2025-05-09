def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        count = countFactor(i)
        if count > limit :
            answer += power
        else:
            answer+=count
    return answer

def countFactor(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            if i * i == num:
                count += 1
            else:
                count += 2
    return count


print(solution(10,3,2))