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