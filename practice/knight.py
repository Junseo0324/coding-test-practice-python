'''
경우의 수
        x : [1,1,2,2,-1,-1,-2,-2]
        y : [2,-2,1,-1,2,-2,1,-1]

        nx = x + dx[i] 를 해서 범위 내에 존재 -> count ++
        a b c d e f g h
        1 2 3 4 5 6 7 8
'''

point = input()
x,y = point[0],int(point[1])-1
type_arr = ['a','b','c','d','e','f','g','h']
dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]

for i in range(len(type_arr)):
    if x == type_arr[i]:
        x = i

count = 0
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx > 7 or ny > 7:
        continue
    count+=1

print(count)

