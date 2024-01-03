class FrequencyTracker:

    def __init__(self):
        self.counter=defaultdict(int)
        self.frequency=defaultdict(int)
       
        

    def add(self, number: int) -> None:
        self.frequency[self.counter[number]]-=1
        self.counter[number]+=1
        self.frequency[self.counter[number]]+=1
        

    def deleteOne(self, number: int) -> None:
        
        if self.counter[number]>0:
            self.frequency[self.counter[number]]-=1
            self.counter[number]-=1
            self.frequency[self.counter[number]]+=1
            
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency[frequency] >0
      
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)