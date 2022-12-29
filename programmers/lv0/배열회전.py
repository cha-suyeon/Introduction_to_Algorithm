# 배열 회전시키기
# 1
def solution(numbers, direction):
    array = []
    n = len(numbers)
    if direction == "left":
        array = numbers[1:]
        array.append(numbers[0])
    else:
        array.append(numbers[-1])
        array.extend(numbers[0:n-1])
    return array

# 2
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]

# 3
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)