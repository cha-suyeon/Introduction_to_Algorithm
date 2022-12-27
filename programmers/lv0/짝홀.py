# 짝수 홀수 개수
# 1
def solution(num_list):
    odd = 0
    even = 0
    answer = []
    for i in num_list:
        if i % 2 ==0:
            even += 1
        else:
            odd += 1
    answer.append(even)
    answer.append(odd)
    return answer

# 2
def solution(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n % 2] += 1
    return answer

num_list = [1, 2, 3, 4, 5]
print(solution(num_list))

# 3
def solution(num_list):
    div_num_list = list(map(lambda v: v % 2, num_list))
    return [div_num_list.count(0), div_num_list.count(1)]

num_list = [1, 3, 5, 7]
print(solution(num_list))