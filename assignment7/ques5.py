#. Write a Python Program to check if given array is Monotonic?

def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            increasing = False
            break


    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            decreasing = False
            break

    return increasing or decreasing

array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [1, 3, 2, 5, 4]
print(is_monotonic(array1))
print(is_monotonic(array2)) 
print(is_monotonic(array3)) 
