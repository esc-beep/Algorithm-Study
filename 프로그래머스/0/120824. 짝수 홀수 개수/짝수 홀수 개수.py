def solution(num_list):
    tmp = 0
    for i in num_list:
        if i % 2 == 0: tmp += 1
    answer = [tmp, len(num_list) - tmp]
    return answer