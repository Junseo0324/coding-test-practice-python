def solution(price, money, count):
    pay =0
    for i in range(1,count+1):
        pay +=i*price
    if pay - money > 0:
        return pay - money
    else :
        return 0

print(solution(3,20,4))