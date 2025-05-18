# 0 x ? = 0
# if num == 0 일 경우 -> 무조건 더하기가 큼.
# 1 X ?  num == 1 일 경우 => 무조건 더하기.

s = input()
result = int(s[0])

for i in range(1,len(s)):
    num = int(s[i])
    if num <=1 or result <=1:
        result +=num
    else:
        result *= num

print(result)

