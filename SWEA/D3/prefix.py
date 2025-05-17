# 2
# 3 3
# able
# abl
# abroad
# ab
# abo
# a

# A -> able, able, abroad / B -> ab , abo , a
# B에 속한 문자열 중 A의 접두어인 문자열의 개수

T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int, input().split())
    n_arr = []
    m_arr = []
    for i in range(n):
        n_arr.append(input())
    for i in range(m):
        m_arr.append(input())

    count = 0

    for prefix in m_arr:
        for word in n_arr:
            if word.startswith(prefix):
                count+=1
                break

    print("#"+str(test_case)+" "+str(count))
