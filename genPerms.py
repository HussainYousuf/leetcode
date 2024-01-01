def rightRotate(arr):
    arr = arr.copy()
    x = arr.pop()
    return [x] + arr


# 1 [2,3] = [[1,2,3], [2,1,3], [2,3,1]]
def insert(x, arr):
    res = []
    newArr = [x] + arr
    for i in range(len(newArr)):
        newArr = rightRotate(newArr)
        res.append(newArr)
    return res


def concat(arr):
    res = []
    for i in arr:
        res += i
    return res


# [] -> [[]]
def genPerms(arr):
    if arr == []:
        return [[]]
    return concat([insert(arr[0], i) for i in genPerms(arr[1:])])


print([1, 2, 3] in genPerms([1, 2, 3]))
