class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = 2
        self.arr = [0] * self.max_size
        self.front = 0
        self.back = 0
        self.size = 0
        self.k = k
    # O(n) but ammortized constant
    def _resize(self):
        temp = [0] * (self.max_size * 2)
        for i in range(self.size):
            temp[i] = self.arr[(self.front + i) % self.max_size]
        self.max_size *= 2
        self.front = 0
        self.back = self.size
        self.arr = temp

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.size == self.max_size:
            self._resize()
        self.arr[self.back] = value
        self.back = (self.back + 1) % self.max_size
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.back - 1) % self.max_size]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()