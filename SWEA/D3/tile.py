# 다음과 같이 2x1, 2x2, 2x3 크기의 타일을 2xN 크기의 공간에 붙이려고 한다. N이 주어지면 붙이는 방법이 모두 몇 가지가 경우가 있는지 출력하는 프로그램을 만드시오.
#
# 예를 들어 N이 3인 경우 타일을 붙이는 방법은 다음과 같다.

#SWEA 5255
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    array = [-1]*(N+1)
    for i in range(1,N+1):
        if i ==1:
            array[i] = 1
        elif i==2:
            array[i] = 3
        elif i == 3:
            array[i] = 6
        else:
            array[i] = array[i-1]+2*array[i-2] + array[i-3]
    print("#"+str(test_case)+" "+str(array[N]))