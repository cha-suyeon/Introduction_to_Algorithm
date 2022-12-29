# 구슬을 나누는 경우의 수
# 1
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
    
def solution(balls, share):
    answer = factorial(balls) // (factorial(balls-share) * factorial(share))
    return answer

# 2
import math
def solution(balls, share):
    return math.comb(balls, share)

# 3
def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result