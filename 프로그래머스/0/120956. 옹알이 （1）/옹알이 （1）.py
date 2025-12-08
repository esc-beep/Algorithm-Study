def solution(babbling):
    answer = 0
    for i in babbling:
        for j in range(0, 4):
            if i.startswith("aya"): i = i[len("aya"):]
            if i.startswith("woo"): i = i[len("woo"):]
            if i.startswith("ye"): i = i[len("ye"):]
            if i.startswith("ma"): i = i[len("ma"):]
        if len(i) == 0: 
            answer += 1
    return answer