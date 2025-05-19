def dfs(num_str,depth):
    global answer

    if depth == change:
        answer = max(answer,int(num_str))
        return

    for i in range(len(num_str)):
        for j in range(i+1,len(num_str)):
            num_list = list(num_str)
            num_list[i], num_list[j] = num_list[j],num_list[i]
            new_number = ''.join(num_list)

            if (new_number,depth+1) not in visited:
                visited.add((new_number,depth+1))
                dfs(new_number,depth+1)



T = int(input())
for test_case in range(1, T + 1):
    num_str,change = input().split()
    change = int(change)
    answer = 0
    visited = set()
    dfs(num_str,0)

    print(f"#{test_case} {answer}")


