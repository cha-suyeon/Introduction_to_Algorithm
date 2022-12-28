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
# print(solution(array, height))

# 외계행성의 나이
# 1
def solution(age):
    alpha = 'abcdefghij'
    lst = list(alpha)
    answer = ''
    for i in str(age): # 23 -> 2, 3
        answer += lst[int(i)]    
    return answer

# 2
def solution(age):
    return ''.join([chr(int(i)+97) for i in str(age)])

# 진료 순서 정하기
# 1
def solution(emergency):
    emerge = sorted(emergency, reverse=True)
    answer = []
    for i in emergency:
        for j in emerge:
            if i == j:
                idx = emerge.index(i) + 1
                answer.append(idx)
    return answer

# 수정
def solution(emergency):
    emerge = sorted(emergency, reverse=True)
    answer = []
    for i in emergency:
        idx = emerge.index(i) + 1
        answer.append(idx)
    return answer

# 2
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

# 3
def solution(emergency):
    e = sorted(emergency, reverse=True)
    return [e.index(i)+1 for i in emergency]
        