# 모음 제거
# 1
def solution(my_string):
    alpha = ['a', 'e', 'i', 'o', 'u']
    for i in alpha:
        for j in my_string:
            if j == i:
                my_string = my_string.replace(j, '')
    return my_string

print(solution('bus'))
print(solution("nice to meet you"))

# 2
def solution(my_string):
    alpha = ['a', 'e', 'i', 'o', 'u']
    for i in alpha:
        if i in my_string:
            my_string = my_string.replace(i, '')
    return my_string

# 3
def solution(my_string):
    return "".join([i for i in my_string if not (i in "aeiou")])

# 문자열 정렬하기