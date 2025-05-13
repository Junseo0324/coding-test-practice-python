
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
    # 구조대 : 119
    # 박준영 : 97 674 223
    # 지영석 : 11 9552 4421

# 정렬을 하게 되면 i+1 과 i 만 비교하면 된다. startswith 함수 사용.
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True


print(solution(["123","456","789"]	))