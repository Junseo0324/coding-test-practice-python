def solution(n):
    word ='수박'
    if n%2==0 :
        return word*(n//2)
    else :
        return word*(n//2)+'수'
    
print(solution(3))