def partition(array, low, high):
    pivot = array[high]
    print('pivot', pivot)
    i = low - 1
    print('i', i) # i = -1, 0, 1, 2, ...
    
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            print('array[i]:', array[i], 'array[j]:', array[j])
            (array[i], array[j]) = (array[j], array[i])
            print('array[i]:', array[i], 'array[j]:', array[j])
     
    (array[i+1], array[high]) = (array[high], array[i+1])
    print('array[i+1]', array[i+1], 'array[high]', array[high])
    print('array', array)
    
    return i + 1

def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        print('pi', pi)
        
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
# array[i+1] -2 array[high] 1
# array [-2, 7, 4, 1, 10, 9, 1]
# pi 0
# pivot 1
# i 0
# array[i]: 7 array[j]: 1
# array[i]: 1 array[j]: 7
# array[i+1] 1 array[high] 4
# array [-2, 1, 1, 7, 10, 9, 4]
# pi 2
# pivot 4
# i 2
# array[i+1] 4 array[high] 7
# array [-2, 1, 1, 4, 10, 9, 7]
# pi 3
# pivot 7
# i 3
# array[i+1] 7 array[high] 10
# array [-2, 1, 1, 4, 7, 9, 10]
# pi 4
# pivot 10
# i 4
# array[i]: 9 array[j]: 9
# array[i]: 9 array[j]: 9
# array[i+1] 10 array[high] 10
# array [-2, 1, 1, 4, 7, 9, 10]
# pi 6
# after sorting [-2, 1, 1, 4, 7, 9, 10]