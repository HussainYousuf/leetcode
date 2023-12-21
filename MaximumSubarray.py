def maxSubarray(arr):
    maxRes = []
    res = []
    maxSum = 0
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum > 0:
            res.append(arr[i])
            if sum > maxSum:
                maxSum = sum
                maxRes = res[:]
        else:
            sum = 0
            res = []

    return (maxRes, maxSum)


print(maxSubarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))
