# Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        
        key = arr[i]
        print('key', key)
        
        # Move elements of arr[0, ..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]       # moved forward
            print('first move',arr)
            j -= 1
        arr[j+1] = key # key is moved to arr[j+1] position
        print('Second move',arr)

        
# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
lst = [] # empty list to store sorted elements

for i in range(len(arr)):
    lst.append(arr[i])
print(lst)                  # appending the elements in sorted order