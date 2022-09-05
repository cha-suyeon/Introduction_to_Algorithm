unsorted_list = [12, 3, 2, 8, 5]

def insertion_sort(unsorted_list):
    j = 1
    for j in range(j, len(unsorted_list)):
        key = unsorted_list[j]
        1 
        i = j-1
        
        while i >= 0 and unsorted_list[i] > key:
            unsorted_list[i+1] = unsorted_list[i]
            i = i - 1
        unsorted_list[i+1] = key
    
    # print(unsorted_list)
    
    return unsorted_list

# sorted_list = insertion_sort(unsorted_list)
# print(sorted_list)

print(insertion_sort(unsorted_list))