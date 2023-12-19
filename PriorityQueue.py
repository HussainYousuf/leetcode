from Heap import Heap
import math


class PriorityQueue:
    def __init__(self, arr) -> None:
        self.heap = Heap(arr).buildHeap()

    def __str__(self) -> str:
        return self.heap.__str__()

    def peek(self):
        return self.heap.arr[1]

    def pop(
        self,
    ):  # this method only works for root, see counterexample at non root: https://walkccc.me/CLRS/Chap06/6.5/
        res = self.peek()
        arr = self.heap.arr
        arr[1] = arr[self.heap.size]
        self.heap.size -= 1
        self.heap.maxHeapify(1)
        return res

    # we need to use a bottom up method (trickle up) for impl insertions, as nodes can only be inserted at leafs
    # we only need increase-key situation but I will impl decrease-key as well
    def update(self, i, newVal):
        arr = self.heap.arr
        oldVal = arr[i]
        arr[i] = newVal
        if oldVal > newVal:  # this will nvr get used in add
            self.heap.maxHeapify(i)
        if oldVal < newVal:
            j = i
            parent = self.heap.parent(j)
            while j > 1 and arr[parent] < arr[j]:
                arr[parent], arr[j] = arr[j], arr[parent]
                j = parent
                parent = self.heap.parent(j)

        return self

    def append(self, val):
        self.heap.size += 1
        self.heap.arr.append(-math.inf)
        return self.update(self.heap.size, val)

    def delete(self, i):
        self.update(i, math.inf)
        self.pop()
        return self


# print(PriorityQueue([16, 14, 10, 8, 7, 9, 3, 2, 4, 1]))
# print(PriorityQueue([16, 14, 10, 8, 7, 9, 3, 2, 4, 1]).update(9, 15))
a = PriorityQueue([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]).append(10)
a = PriorityQueue([15, 7, 9, 1, 2, 3, 8])
print(a)
a.delete(5)
print(a)
print(a.heap.isHeap())
