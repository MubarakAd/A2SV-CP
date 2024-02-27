class RecentCounter:

    def __init__(self):
        self.dequeue=deque()
        

    def ping(self, t: int) -> int:
        if len(self.dequeue)==0:
            self.dequeue.append(t)
            return len(self.dequeue)
        else:
            while len(self.dequeue)!=0 and t-self.dequeue[0]>3000:
                self.dequeue.popleft()
            self.dequeue.append(t)
            return len(self.dequeue)

        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)