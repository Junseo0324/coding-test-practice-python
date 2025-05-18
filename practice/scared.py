# 1 2 2 2 3 1
# 3 2 2 / 2 2 /2
n = int(input())
arr = list(map(int,input().split()))

arr = sorted(arr,reverse=True)

group_count = 0
temp = []
member = 0
for i in range(len(arr)+1):
    if member == 0:
        member = arr[i]
        temp.append(arr[i])
    else :
        if not len(temp) == member:
            temp.append(arr[i])
        else:
            group_count +=1
            temp = []
            member = 0

print(group_count)


'''
    오름차순 후 -> 공포도가 낮은 모험가부터 확인
    현재 그룹에 포함된 모험가 수 
'''

n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0
count = 0
for i in data:
    count+=1
    if count >= i :
        result +=1
        count = 0
