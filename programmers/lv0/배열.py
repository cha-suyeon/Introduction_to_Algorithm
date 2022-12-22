# 나머지 구하기
def solution(num1, num2):
    answer = num1 % num2
    return answer

# 중앙값 구하기
# 1
def solution(array):
    array.sort()
    n = len(array)
    answer = array[n//2]
    return answer

arr = [1, 2, 7, 10, 11]
print(solution(arr))
arr2 = [9, -1, 0]
print(solution(arr2))

# 2
def solution(array):
    return sorted(array)[len(array)//2]

# 짝수는 싫어요
# 1
def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2:
            answer.append(i) 
    return answer
print(solution(10))

# 2
def solution(n):
    return [i for i in range(1, n+1, 2)]
print(solution(15))