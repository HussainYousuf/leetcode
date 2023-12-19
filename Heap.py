# I ll use 1-indexing as I am following CLRS


class Heap:
    def __init__(self, arr) -> None:
        self.arr = [None, *arr]
        self.size = len(arr)  # i ll be able to index 'size' b/c of 1-based indexing
        # self.buildHeap()

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    # here we r assuming that children, left and right satisfy the HEAP property
    def maxHeapify(self, i):
        size = self.size
        arr = self.arr
        left = self.left(i)
        right = self.right(i)
        largest = i

        if left <= size and arr[left] > arr[i]:
            largest = left

        if right <= size and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.maxHeapify(largest)  # base-case when reached leafs (no left or right)

    # b/c of the above assumption w r building heap in bottom up manner from node just above leafs
    # b/c leafs (single node) satisfy HEAP property
    def buildHeap(self):
        n = self.size
        # leafs are indexes [n//2+k , n] where k > 0
        # going in descending order from n//2 to 1 will hit every parent of leaf and parent's parent
        for i in range(n // 2, 0, -1):
            self.maxHeapify(i)

        return self

    def __str__(self) -> str:
        return str(self.arr[1:]) + " len: " + str(self.size)

    # idea is simple take the largest (index == 1) and replace it with last index, apply maxHeapify on index 1 to maintain HEAP property
    def sort(self):
        n = self.size
        arr = self.arr
        for i in range(n, 0, -1):
            arr[i], arr[1] = arr[1], arr[i]  # exchange
            self.size -= 1  # in maxHeapify don't include last-element b/c it wud go up
            self.maxHeapify(1)

        self.size = n
        return self

    def isHeap(self):
        arr = self.arr
        for i in range(2, self.size):
            if arr[self.parent(i)] < arr[i]:
                print(
                    "heap prop violated: "
                    + str(arr[self.parent(i)])
                    + "-parent is less than "
                    + str(arr[i])
                    + "-child"
                )
                return False
        return True


# print(Heap([1, 8.5, 7, 8, 5, 4, 3]).isHeap())
