# 최댓값 만들기
# 1
def solution(numbers):
    first = max(numbers)
    second = sorted(numbers)[-2]
    answer = first * second
    return answer

# 2
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]

# 삼각형의 완성조건
# 1
def solution(sides):
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        return 1
    else:
        return 2
    
# 2
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2