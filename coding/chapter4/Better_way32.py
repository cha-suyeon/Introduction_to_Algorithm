# 파일에서 읽은 x에는 새줄 문자가 들어 있으므로 길이가 눈에 보이는 길이보다 1만큼 더 길다

value = [len(x) for x in open('my_file.txt')]
print(value)

it= (len(x) for x in open('my_file.txt'))
print(it)

print(next(it))
print(next(it))

root = ((x, x**0.5) for x in it)
print(next(root))

