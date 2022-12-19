def partition(array, low, high):
    pivot = array[high]
    print('pivot', pivot)
    i = low - 1
    print('i', i) # i = -1, 0, 1, 2, ...
    
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            
            (array[i], array[j]) = (array[j], array[i])
            
    (array[i+1], array[high]) = (array[high], array[i+1])
    print('array', array)
    
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
        
data = [1, 7, 4, 1, 10, 9, -2]
print('origin data', data)
size = len(data)

quickSort(data, 0, size - 1)
print('after sorting', data)

# origin data [1, 7, 4, 1, 10, 9, -2]
# pivot -2
# i -1
# array [-2, 7, 4, 1, 10, 9, 1]
# pivot 1
# i 0
# array [-2, 1, 1, 7, 10, 9, 4]
# pivot 4
# i 2
# array [-2, 1, 1, 4, 10, 9, 7]
# pivot 7
# i 3
# array [-2, 1, 1, 4, 7, 9, 10]
# pivot 10
# i 4
# array [-2, 1, 1, 4, 7, 9, 10]
# after sorting [-2, 1, 1, 4, 7, 9, 10]