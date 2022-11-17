a = b'h\x65llo'
print(list(a))
print(a)

# [104, 101, 108, 108, 111]
# b'hello'

a = 'a\u0300 propos'
print(list(a))
print(a)

# ['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']
# à propos

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # str 인스턴스

print(repr(to_str(b'foo')))
print(repr(to_str('bar')))
print(repr(to_str(b'\xed\x95\x9c'))) # UTF-8에서 한글은 3바이트임

# 'foo'
# 'bar'
# '한'

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # bytes 인스턴스

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
print(repr(to_bytes('한글'))) 

# b'foo'
# b'bar'
# b'\xed\x95\x9c\xea\xb8\x80'

print(b'one' + b'two')
print('one' + 'two')

# b'onetwo'
# onetwo

# Wrong
# print(b'one' + 'two')
# print('one' + b'two')

print(b'foo' == 'foo')

# False

print(b'red %s' % b'blue')
print('red %s' % 'blue')

# b'red blue'
# red blue

# wrong
# print(b'red %s' % 'blue')

print('red %s' % b'blue')

# red b’blue’

# Error
# with open('data.bin', 'w') as f:
#     f.write(b'\xf1\xf2\xf3\xf4\xf5')
    
# TypeError: write() argument must be str, not bytes

with open('data.bin', 'wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')

# Error
# with open('data.bin', 'r') as f:
#     f.write(b'\xf1\xf2\xf3\xf4\xf5')

# UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0xf1 in …
    
with open('data.bin', 'rb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')
    
with open('data.bin', 'r', encoding='cp1252') as f:
    data = f.read()

assert data == 'ñòóôõ'

# 시스템 디폴트 인코딩 검사
# python3 -c 'import locale; print(locale.getpreferredencoding())'