def solution(my_string):
    answer = ''
    for string in my_string:
        if string != 'a' and string !='e' and string !='i' and string !='o' and string !='u':
            answer += string
    return answer