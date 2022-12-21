# 두 수의 합
def solution(num1, num2):
    answer = num1 + num2
    return answer

# 두 수의 차
def solution(num1, num2):
    answer = num1 - num2
    return answer

# 두 수의 곱
def solution(num1, num2):
    answer = num1 * num2
    return answer

# 몫 구하기
def solution(num1, num2):
    answer = num1 // num2
    return answer

# 두 수의 나눗셈
def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer

# 숫자 비교하기
# 1
def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer
# 2
def solution(num1, num2):
    return 1 if num1 == num2 else -1


# 배열 두 배 만들기
# 1
def solution(numbers):
    answer = [2*i for i in numbers]
    return answer

# 2
def solution(numbers):
    return list(map(lambda x: x * 2, numbers))

# 분수의 덧셈
# ver2
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(denum1, num1, denum2, num2):
    # 1. 두 분수의 합 계산
    boonmo = num1 * num2
    boonja = denum1 * num2 + denum2 * num1
    
    # 2. 최대공약수 계산
    gcd_value = gcd(boonmo, boonja)

    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [int(boonja / gcd_value), int(boonmo / gcd_value)]
    return answer

denum1 = 1
num1 = 2
denum2 = 3
num2 = 4

print(solution(denum1, num1, denum2, num2))