class MyQueue:

    def __init__(self):
        self.arr = []
        self.top = -1

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        self.top += 1
        if self.top < len(self.arr):
            return self.arr[self.top]

    def peek(self) -> int:
        if self.top + 1 < len(self.arr):
            return self.arr[self.top + 1]

    def empty(self) -> bool:
        if self.top + 1 < len(self.arr):
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
