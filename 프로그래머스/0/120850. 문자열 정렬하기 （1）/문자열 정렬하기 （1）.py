def solution(my_string):
    answer = []
    for i in range(0, len(my_string)):
        if my_string[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            answer.append(int(my_string[i]))
    answer.sort()
    return answer