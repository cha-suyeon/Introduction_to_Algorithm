# 옷가게 할인 받기

# 1
def solution(price: int)  -> int:
    if price >= 500000:
        return int(price * 0.80)
    elif price >= 300000:
        return int(price * 0.90)
    elif price >= 100000:
        return int(price * 0.95)
    return price

print(solution(150000))

# 2
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
        
print(solution(150000))
