# 숨어있는 숫자의 덧셈
# 1
import re

def solution(my_string):
    answer = re.findall(r'\d', my_string)
    print(answer)
    answer = [int(i) for i in answer]
    return sum(answer)

print(solution("aAb1B2cC34oOp"))

# 2
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

print(solution("aAb1B2cC34oOp"))