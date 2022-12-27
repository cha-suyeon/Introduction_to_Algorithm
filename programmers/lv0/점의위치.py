# 점의 위치 구하기
# 1
def solution(dot):
    if dot[1] > 0:
        if dot[0] > 0:
            return 1
        else:
            return 2
    else:
        if dot[0] >0:
            return 4
        else:
            return 3

# 2
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]

print(solution([2, 4]))
dot = [2, 4]
print(dot[0]>0)
quad = [(3,2),(4,1)]
print(quad[True][False])