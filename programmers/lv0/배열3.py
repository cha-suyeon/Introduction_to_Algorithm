# 배열 원소의 길이
# 1
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# 2
def solution(strlist):
    return [len(str) for str in strlist]

# 배열자르기
def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer

# 배열의 유사도
# 1
def solution(s1, s2):
    count = 0
    for i in s1:
        for j in s2:
            if i == j:
                count += 1
    return count

# 2
def solution(s1, s2):
    return len(set(s1) & set(s2))

# s1 = ["a", "b", "c"]
# s2 = ["com", "b", "d", "p", "c"]
# print(set(s1)&set(s2))