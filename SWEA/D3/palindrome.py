def is_palindrome(s):
    return s == s[::-1]


for test_case in range(1, 11):
    n = int(input())
    word_arr = [list(input()) for _ in range(8)]

    answer = 0
    for i in range(8):
        for j in range(8 - n + 1):
            if is_palindrome(word_arr[i][j:j+n]):
                answer+=1

            col_str = ''.join(word_arr[j+k][i] for k in range(n))
            if is_palindrome(col_str):
                answer+=1

    print(f"#{test_case} {answer}")