def solution(n, m):
    answer = [gcd(n,m),lcm(n,m)]
    return answer

def gcd(n,m):
    if m==0 : return n 
    else : return gcd(m,n%m)

def lcm(n,m):
    return abs(n*m) // gcd(n,m)


print(solution(3,12))