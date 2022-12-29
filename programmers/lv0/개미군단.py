# 개미 군단
# 1
def solution(hp):
    first = hp // 5
    hp -= first * 5
    second = hp // 3
    hp -= second * 3
    third = hp // 1
    answer = first + second + third
    return answer

# 2
def solution(hp):
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

# 3
def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer