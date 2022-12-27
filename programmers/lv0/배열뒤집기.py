# 배열 뒤집기
# 1
def solution(num_list):
    num_list.reverse()
    return num_list

# 2
def solution(num_list):
    return num_list[::-1]

# 3
def solution(num_list):
    result = []
    while (num_list):
        result.append(num_list.pop())
    return result
    
num_list = [1, 0, 1, 1, 1, 3, 5]