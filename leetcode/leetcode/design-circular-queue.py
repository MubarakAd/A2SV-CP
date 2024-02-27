class MyCircularQueue:

    def __init__(self, k: int):
        self.my_queue=deque()
        self.k=k
    def enQueue(self, value: int) -> bool:
        if len(self.my_queue)<self.k:
            self.my_queue.append(value)
            return True
        return False
        

    def deQueue(self) -> bool:
        if len(self.my_queue)!=0:
            self.my_queue.popleft()
            return True
        return False

    def Front(self) -> int:
        if len(self.my_queue)!=0:
            return self.my_queue[0]
        return -1
        

    def Rear(self) -> int:
        if len(self.my_queue)!=0:
            return self.my_queue[-1]
        return -1
        

    def isEmpty(self) -> bool:
        if len(self.my_queue)==0:
            return True
        return False
    def isFull(self) -> bool:
        if len(self.my_queue)>=self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()