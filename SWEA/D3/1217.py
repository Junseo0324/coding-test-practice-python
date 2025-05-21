#다음과 같이 두 개의 숫자 N, M이 주어질 때, N의 M 거듭제곱 값을 구하는 프로그램을 재귀호출을 이용하여 구현해 보아라.

def recurisonFun(num,c):
    if c <=1:
        return num
    return num * recurisonFun(num,c-1)

for test_case in range(1, 11):
    num = int(input())
    n, m = map(int,input().split())

    print(f"#{test_case} {recurisonFun(n,m)}")
