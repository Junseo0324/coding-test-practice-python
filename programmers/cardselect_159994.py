def solution(cards1, cards2, goal):
    cards1_idx = 0
    cards2_idx = 0
    for word in goal :
        if word == cards1[cards1_idx] :
            if cards1_idx < len(cards1)-1:
                cards1_idx+=1
        elif word == cards2[cards2_idx] :
            if cards2_idx < len(cards2)-1 :
                cards2_idx+=1
        else :
            return "No"

    return "Yes"

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))