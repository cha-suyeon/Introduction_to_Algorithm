# 2차원으로 만들기
# 1
def solution(num_list, n):
    answer = []
    for i in range(n, len(num_list)+1, n):
        answer.append(num_list[i-n:i])
    return answer

# 2
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        print(i)
        answer.append(num_list[i:i+n])
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))

# 3
def solution(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]

