# 순서쌍의 개수
# 1
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.extend([(i, n//i)])
            print(answer)
    return len(answer)

print(solution(20))

# 2
def solution(n):
    return len(list(filter(lambda v: n & (v+1) == 0, range(n))))