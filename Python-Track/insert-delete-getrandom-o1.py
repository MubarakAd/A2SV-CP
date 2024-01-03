class RandomizedSet:

    def __init__(self):
        self.sett=set()
        

    def insert(self, val: int) -> bool:
        if val not in self.sett:
            self.sett.add(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.sett:
            self.sett.discard(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        if len(self.sett)!=0:
            return random.choice(list(self.sett))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()