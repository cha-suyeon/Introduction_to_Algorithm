a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('가운데 2개:', a[3:5])
print('마지막을 제외한 나머지:', a[1:7])


a[:]
a[:5]
a[:-1]
a[4:]
a[-3:]
a[2:5]
a[2:-1]
a[-3:-1]


first_twenty_items = a[:20]
last_twenty_items = a[-20:]


# a[20] # error
# IndexError: list index out of range


b = a[3:]
print('이전:', b)
b[1] = 99
print('이후:', b)
print('변화없음:', a)


print('이전:', a)
a[2:7] = [99, 22, 14]
print('이후:', a)


print('이전:', a)
a[2:3] = [47, 11]
print('이후:', a)


b = a[:]
assert b == a and b is not a


b = a[:]
assert b == a and b is not a
# a[:] = [101, 102, 103]
print('이후 a:', a) 
print('이전 b:', b) 


b = a
print('이전 a:', a)
print('이전 b:', b)
a[:] = [101, 102, 103]
assert a is b # 여전히 같은 리스트 객체임
print('이후 a:', a) # 새로운 내용이 들어 있음
print('이후 b:', b) # 같은 리스트 객체이기 때문에 a와 내용이 같음