def is_palindrome(s):
    return s == s[::-1]

for test_case in range(1, 11):
    n = int(input())
    word_arr = [list(input()) for _ in range(100)]


    answer = 0
    for i in range(1,101): # n 이라고 생각
        for j in range(100):
            for k in range(100 - i +1):
                if is_palindrome(word_arr[j][k:k+i]):
                    answer = max(answer,i)

                col_str = ''.join(word_arr[k+m][j] for m in range(i))
                if is_palindrome(col_str) :
                    answer = max(answer,i)

    print(f"#{n} {answer}")