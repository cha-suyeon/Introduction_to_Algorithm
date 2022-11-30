x = ['빨강', '주황', '노랑', '초록', '파랑', '자주']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)


x = b'mongoose'
y = x[::-1]
print(y)


x = '차수연'
y = x[::-1]
print(y)


w = '차수연'
# x = w.encode('utf-8')
y = x[::-1]
print(y)


x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(x[::2])
print(x[::-2])


w ='abcZYX123'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')
print(z)


x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(x[2::2])
print(x[-2::-2])
print(x[-2:2:-2])
print(x[2:2:-2])


y = x[::2]
print(y)
z = y[1:-1]
print(z)