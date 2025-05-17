T = int(input())
for test_case in range(1, T+1):
    k, word = map(str,input().split())
    word_list = set()
    for i in range(len(word)):
        for j in range(i+1,len(word)+1):
            word_list.add(word[i:j])

    sorted_list = sorted(word_list)

    print("#"+str(test_case)+" "+str(sorted_list[int(k)-1][0] + " "+str(len(sorted_list[int(k)-1]))))
