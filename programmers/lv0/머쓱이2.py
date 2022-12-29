# 편지
def solution(message):
    answer = 0
    for i in message:
        answer += 2
    return answer

def solution(message):
    return len(message) * 2

# 공 던지기
# 1
def solution(numbers, k):
    k = 2 * (k - 1) % len(numbers)
    return numbers[k]

# 2
from collections import deque
def solution(numbers, k):
    array = deque(numbers)
    print(array)
    array.rotate(-(k-1)*2)
    print(array)
    return array[0]

print(solution([1, 2, 3, 4], 2))