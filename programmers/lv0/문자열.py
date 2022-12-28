# 문자열 뒤집기
# 1
def solution(my_string):
    return my_string[::-1]

# 2 
def solution(my_string):
    answer = ''
    for i in range(len(my_string)-1, -1, -1):
        answer += my_string
    return answer

# 문자열 반복
# 1
def solution(my_string, n):
    answer = []
    for i in my_string:
           answer.append(i*n)
    return "".join(answer)
    
my_string = "hello"
print(solution(my_string, 3))

# 2
def solution(my_string, n):
    return ''.join(i*n for i in my_string)

my_string = "dahun"
print(solution(my_string, 3))

# 특정 문자 제거하기
# 1
def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer

# 2
def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            asnwer += string
    return answer

# 3
def solution(my_string, letter):
    return ''.join([c for c in my_string if c != letter])


# 문자열 안에 문자열
# 1
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2
    
# 2
def solution(str1, str2):
    return 1 if str2 in str1 else 2