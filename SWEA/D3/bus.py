# 0 -> 최대 갈 수 있는 거리가 curr + k , 이 값이 list 에 in 이라면 그곳으로 아니라면
# 그 전에 가장 가까운곳에서 충전.
# 3 10 5
# 1 3 5 7 9
# 0-> 3 -> 5 -> 7 -> 10
# bus_arr[i] -> 1, bus_arr[i+1] -> 3
# if bus_Arr[i] < curr+k <= i+1 -> i +=1 , count +=1
# elif bus_arr[i] > curr+k -> return 0
# elif bus_arr[i], bus_arr[i+1] < curr

T = int(input())
for test_case in range(1, T+1):
    k,n,m = map(int,input().split())
    bus_arr = list(map(int,input().split()))

    bus_arr = [0] + bus_arr + [n]
    curr = 0
    count = 0
    for i in range(1,len(bus_arr)):
        if bus_arr[i] - bus_arr[i-1] > k:
            count = 0
            break
        if bus_arr[i] > curr+k :
            curr = bus_arr[i-1]
            count+=1

    print("#"+str(test_case)+" "+str(count))


