# 아이스 아메리카노
# 1
def solution(money):
    answer = []
    count = money // 5500 
    answer.append(count)
    cash = money % 5500
    answer.append(cash)
    return answer

# 2
def solution(money):
    answer = [money // 5500, money % 5500]
    return answer

money = 5500
print(solution(money))
money = 15000
print(solution(money))