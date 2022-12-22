# 최빈값 구하기

# 1
def solution(array):
    dict = {}
    
    for i in array:
        dict.setdefault(i, 0)
        dict[i] += 1
    dict = sorted(((value, key) for key, value in dict.items()), reverse=True)
    
    if len(dict) > 1:
        return dict[0][1] if dict[0][0] != dict[1][0] else -1
    return dict[0][1]

arr1 = [1, 2, 3, 3, 3, 4]
arr2 = [1, 1, 2, 2]
arr3 = [1]

# 2
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            # print('i', i, 'a', a)
            array.remove(a)
            # print(array)
        if i == 0: return a
    return -1

arr4 = [4, 4, 4, 3, 2, 2]
print('set', set(arr4))
print(solution(arr4))



# 3
