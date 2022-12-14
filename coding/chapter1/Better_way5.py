from urllib.parse import parse_qs

my_values = parse_qs('빨강=5&파랑=0&초록=', keep_blank_values=True)

print(repr(my_values))
# {'빨강': ['5'], '파랑': ['0'], '초록': ['']}


print('빨강:', my_values.get('빨강'))
print('초록:', my_values.get('초록'))
print('투명도:', my_values.get('투명도'))
# 빨강: ['5']
# 초록: ['']
# 투명도: None


# 질의 문자열이 '빨강=5&파랑=0&초록='인 경우
red = my_values.get('빨강', [''])[0] or 0
green = my_values.get('초록', [''])[0] or 0
opacity = my_values.get('투명도', [''])[0] or 0
print(f'빨강: {red!r}')
print(f'초록: {green!r}')
print(f'투명도: {opacity!r}')
# 빨강: '5'
# 초록: 0
# 투명도: 0


red = int(my_values.get('빨강', [''])[0]) or 0
print(red) # 5


red_str = my_values.get('빨강', [''])
red = int(red_str[0]) if red_str[0] else 0
print(red) # 5


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

green = get_first_int(my_values, '초록')
print('green', green)
# green 0