# Quick Sort
# 확인용 코드 전부 주석 처리

def partition(array, low, high):
    pivot = array[high]
    # print('pivot', pivot)
    i = low - 1
    # print('i', i) # i = -1, 0, 1, 2, ...
    
    for j in range(low, high): # j = 0, ..., 5 
        if array[j] <= pivot:
            # print('array[j]', array[j])
            i = i + 1
            # print('Before swapping: array[i]:', array[i], 'array[j]:', array[j])
            (array[i], array[j]) = (array[j], array[i])
            # print('After swapping: array[i]:', array[i], 'array[j]:', array[j])
    
    # print('before array', array)
    # print('array[i+1]', array[i+1], 'array[high]', array[high])
    (array[i+1], array[high]) = (array[high], array[i+1])
    # print('array', array)
    
    return i + 1

def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        # print('pi', pi)
        
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
        
data = [1, 7, 4, 1, 10, 9, -2]
print('origin data', data)
size = len(data)

quickSort(data, 0, size - 1)
print('after sorting', data)
