# Quick Sort
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot, tail = array[0], array[1:]
    
    leftside = [x for x in tail if x <= pivot]
    rightside = [x for x in tail if x > pivot]
    
    # 출력 확인 코드
    print('pivot', pivot)
    print("leftside", leftside)
    print("rightside", rightside)
    
    return quick_sort(leftside) + [pivot] + quick_sort(rightside)

array = [1, 7, 4, 1, 10, 9, -2]
print(quick_sort(array))

# pivot 1
# leftside [1, -2]       
# rightside [7, 4, 10, 9]
# pivot 1
# leftside [-2]
# rightside []
# pivot 7
# leftside [4]
# rightside [10, 9]      
# pivot 10
# leftside [9]
# rightside []
# [-2, 1, 1, 4, 7, 9, 10]