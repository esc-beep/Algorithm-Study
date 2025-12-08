def solution(array):
    max = 0
    index = 0
    count = 0
    for i in array:
        if i > max:
            max = i
            index = count
        count += 1
    answer = [max, index]
    return answer