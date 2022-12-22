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

# 짝수의 합
# 1
def solution(n):
    answer = [i for i in range(0, n+1, 2)]
    answer = sum(answer)
    return answer

# 2
def solution(n):
    return sum([i for i in range(2, n+1, 2)])

# 양꼬치
def solution(n, k):
    answer = 12000 * n + (k - n // 10) * 2000
    return answer

print(solution(10,3))
print(solution(22,9))

# 중복된 숫자 개수
# 1
def solution(array, n):
    count = 0
    for i in array:
        if i == n:
            count += 1
    return count

# 2
def solution(array, n):
    return array.count(n)

# 3
def solution(array, n):
    return sum(1 for x in array if x == n)