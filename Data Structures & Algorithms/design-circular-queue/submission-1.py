class Node:
    def __init__(self, val = 0):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.front = None
        self.back = None
        self.size = 0
        

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        node = Node(value)
        if self.back is None:
            self.back = node
        else:
            node.prev = self.back
            self.back.next = node
            self.back = node
        if self.front is None:
            self.front = node
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        node = self.front
        if self.size == 1:
            # node prev == None
            self.front = None
            self.back = None
        else:
            self.front = node.next
            node.next.prev = None
        self.size -= 1
        return True

        

    def Front(self) -> int:
        if self.front is None:
            return -1
        return self.front.val

    def Rear(self) -> int:
        if self.back is None:
            return -1
        return self.back.val
        

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