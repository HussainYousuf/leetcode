def selectionSort(arr):
    for i in range(0, len(arr)):
        smallest = arr[i]
        j = i + 1
        while j < len(arr):
            if arr[j] < smallest:
                smallest = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr
