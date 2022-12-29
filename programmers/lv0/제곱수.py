# 제곱수 판별하기
# 1
def solution(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return 1
    else:
        return 2
    
# 2
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

# 3
def solution(n):
    if n ** (1/2) == int(n**(1/2)):
        return 1
    else:
        return 2