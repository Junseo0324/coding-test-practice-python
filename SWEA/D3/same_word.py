T = int(input())
for test_case in range(1, T+1):
    a,b = map(int,input().split())

    a_arr = [input().strip() for _ in range(a)]
    b_arr = [input().strip() for _ in range(b)]
    count = 0
    for word in  a_arr:
        if word in b_arr:
            count+=1

    print("#"+str(test_case)+" "+str(count))

