# 길이 = n , 룰러 길이 = m , section = 칠해야하는 구여
# 페인트칠 해야하는 최소 횟수
#  Boolean 으로 칠해야 하는 곳을 지정 후
#  paint 배열을 for 문을 돌며 false인 i 지점부터 +m 까지 true로 변경 하면서 answer++
# if 모두 다 true 이면 종료.

def solution(n, m, section):
    answer = 0
    paint = [True]*n
    for sec in section:
        if paint[sec-1] :
            paint[sec-1] = False

    for i in range(len(paint)):
        if not paint[i]:
            for j in range(i,i+m):
                if j >= len(paint): break
                paint[j] = True
            answer +=1
    return answer


print(solution(8,4,[2,3,6]))