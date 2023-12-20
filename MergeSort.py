def merge(arr, startIndex, mid, length):
    k = startIndex
    L = arr[startIndex:mid]
    R = arr[mid:length]
    i = 0
    j = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr


def mergeSort(arr, startIndex=None, length=None, comment=None):
    if startIndex is None:
        startIndex = 0
        length = len(arr)

    if length - startIndex <= 1:
        return arr

    mid = (startIndex + length) // 2
    mergeSort(arr, startIndex, mid)
    mergeSort(arr, mid, length)

    return merge(arr, startIndex, mid, length)


print(mergeSort([2, 1]))
