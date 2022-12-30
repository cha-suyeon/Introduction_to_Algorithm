# 주사위의 개수
# 1
def solution(box, n):
    answer = (box[0]//n) * (box[1]//n) * (box[2]//n)
    return answer

# 2
def solution(box, n):
    answer = 1
    for b in box:
        answer *= b // n
    return answer

# 합성수 찾기
def solution(n):
    lst = []
    count = 0
    for i in range(2, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                lst.append(i)
        if lst.count(i) >= 3:
            count += 1
    return count

# 팩토리얼
# 1
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
    
def solution(n):
    for i in range(11):
        if n >= factorial(i):
            answer = i
    return answer

print(solution(7))
print(solution(3628800))

# 2
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k

print(solution(3628800))