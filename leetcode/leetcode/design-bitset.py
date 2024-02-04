class Bitset:
    def __init__(self, size: int):
            self.list = [False] * size
            self.listinv = [True] * size
            self.size = size
            self.zeros = size
            self.ones = 0
            self.flips = 0
            
    def fix(self, idx: int) -> None:
        if not self.list[idx]:
            self.list[idx] = True
            self.listinv[idx] = False
            self.ones+=1
            self.zeros-=1

    def unfix(self, idx: int) -> None:
        if self.list[idx]:
            self.list[idx] = False
            self.listinv[idx] = True
            self.ones-=1
            self.zeros+=1

    def flip(self) -> None:
        self.ones,self.zeros = self.zeros,self.ones
        self.list,self.listinv = self.listinv,self.list
        
    def all(self) -> bool:
        return self.ones==self.size

    def one(self) -> bool:
        return self.ones>0

    def count(self) -> int:
        return self.ones
        
    def toString(self) -> str:
        return "".join("1" if i else "0" for i in self.list)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()