# 자릿수 더하기
# 1
def solution(n):
    count = 0
    for i in str(n):
        count += int(i)
    return count

# 2
def solution(n):
    count = sum(list(map(int, list(str(n)))))
    return count

# 3 
def solution(n):
    answer = 0
    while n:
        n, r = divmod(n, 10)
        print('n', n)
        print('r', r)
        answer += r
        print('answer', answer)
    return answer

print(solution(1234))