from random import randint

random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i

print(bin(random_bits))
# 0b11110000010010100110101001111010


flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']
for flavor in flavor_list:
    print(f'{flavor} 맛있어요.')
# 바닐라 맛있어요.
# 초콜릿 맛있어요.
# 피칸 맛있어요.  
# 딸기 맛있어요.


for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i + 1}: {flavor}')
# 1: 바닐라
# 2: 초콜릿
# 3: 피칸
# 4: 딸기


it = enumerate(flavor_list)
print(next(it))
print(next(it))
# (0, '바닐라')
# (1, '초콜릿')


for i, flavor in enumerate(flavor_list):
    print(f'{i+1}: {flavor}')
# 1: 바닐라
# 2: 초콜릿
# 3: 피칸
# 4: 딸기

for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')
# 1: 바닐라
# 2: 초콜릿
# 3: 피칸
# 4: 딸기