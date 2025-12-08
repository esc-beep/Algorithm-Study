import math

def solution(n, k):
    answer = 12000 * n + 2000 * (k-math.floor(n/10))
    return answer