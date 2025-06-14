from collections import deque

for test_case in range(1,2):
    n = int(input())
    queue = deque()
    graph = list(map(int,input().split()))
    for num in graph:
        queue.append(num)
    i = 1
    while queue[-1] != 0:
        curr = queue.popleft()
        if curr - i <0:
            curr = 0
            queue.append(0)
            if i == 5:
                i = 1
            else :i+=1
        elif curr -i>=0:
            queue.append(curr-i)
            if i == 5:
                i = 1
            else :i+=1
    print(f"#{test_case} {' '.join(list(map(str,queue)))}")