def binary_search(arr, target):
    arr.sort()   

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [40, 10, 50, 20, 30]
target = 50

result = binary_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")