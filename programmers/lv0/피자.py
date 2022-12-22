# 피자 나눠 먹기1
# 1
def solution(n):
    if n % 7 == 0:
        answer = n // 7
    else:
        answer = n // 7 + 1
    return answer

# print(solution(7))
# print(solution(1))
# print(solution(15))

# 2
def solution(n):
    return (n-1) // 7 + 1

# 3
import math

def solution(n):
    return math.ceil(n/7) # 올림하여 정수 반환

# 피자 나눠 먹기2
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

# def gcd(a, b):
#     if a % b == 0:
#         return b
#     return gcd(b, a % b)

def lcm(a, b):
    result = (a * b) // gcd(a, b)
    return result

# print(lcm(6,6))
# print(lcm(10,6))
# print(lcm(4,6))

def solution(n):
    value = lcm(n, 6)
    answer = value // 6
    return answer

# print(solution(6))
# print(solution(10))
# print(solution(4))

# 피자 나눠먹기 3
# 1
def solution(slice, n):
    if n % slice == 0:
        answer = n // slice
    else:
        answer = n // slice + 1
    return answer

# 2
def solution(slice, n):
    return (n-1) // slice + 1

# 3
def solution(slice, n):
    d, m = divmod(n, slice) # divmod : 몫과 나머지
    print('d', d)
    print('m', m)
    return d + int(m != 0)

print(solution(7, 10))
print(solution(4, 12))