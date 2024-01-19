class UndergroundSystem:

    def __init__(self):

        self.customer={}
        self.stations=defaultdict(list)
        self.time=0
        self.initial=0
        self.final=0
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id]=[stationName, t]


        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.time= t-self.customer[id][1]
        self.initial=self.customer[id][0]
        self.final=stationName
        self.stations[(self.initial, self.final)].append(self.time)
 
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        li=self.stations[(startStation,endStation)]
        avg=sum(li)/len(li)
        return avg


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)