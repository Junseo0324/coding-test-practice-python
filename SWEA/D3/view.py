'''
0 0 254 185 76 227 84 175 0 0
254-185 = 69
227-185 = 42
-> 111
'''



N = int(input())
buildings = list(map(int, input().strip().split(' ')))
answer = 0
for i in range(2,N-2):
    view_count = 0
    if (buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2]) and (buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]):
        view_count = min(buildings[i]-buildings[i-1],buildings[i]-buildings[i-2],buildings[i]-buildings[i+1],buildings[i]-buildings[i+2])
        answer+=view_count

print(answer)


for test_case in range(1,11):
    N = int(input())
    buildings = list(map(int, input().strip().split(' ')))
    answer = 0
    for i in range(2,N-2):
        view_count = 0
        if (buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2]) and (buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]):
            view_count = min(buildings[i]-buildings[i-1],buildings[i]-buildings[i-2],buildings[i]-buildings[i+1],buildings[i]-buildings[i+2])
            answer+=view_count
    print("#" + str(test_case) +" " + str(answer))
