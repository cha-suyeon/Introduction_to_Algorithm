# 나이 출력
def solution(age):
    answer = 2023 - age
    return answer

# 각도기
def solution(angle):
    if angle >= 180:
        answer = 4
    elif angle > 90:
        answer = 3
    elif angle >= 90:
        answer = 2
    else:
        answer = 1
    return answer

# 배열의 평균값
def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer