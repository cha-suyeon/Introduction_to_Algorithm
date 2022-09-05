import time

start = time.time()
print('start time', start)

arr = [12, 11, 13, 5, 6]


def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                

print(insertion_sort(arr))

end = time.time()

print(round(end-start,6))