def binarySearch(arr, val):
    start = 0
    end = len(arr)
    while start < end:
        middle = (start + end) // 2
        if arr[middle] == val:
            return middle
        if arr[middle] < val:
            start = middle + 1
        if arr[middle] > val:
            end = middle
    return -1


print([binarySearch([7], i) for i in [1, 2, 3, 4, 5, 6, 7]])
