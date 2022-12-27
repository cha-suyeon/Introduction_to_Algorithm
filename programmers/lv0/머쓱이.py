# 머쓱이보다 키 큰 사람

# 1
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

# 2
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

array = [149, 180, 192, 170]
height = 167
print(solution(array, height))