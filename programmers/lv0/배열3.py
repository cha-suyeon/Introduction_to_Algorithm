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