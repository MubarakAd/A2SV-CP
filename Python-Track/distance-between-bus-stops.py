class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sum=0
        _all=0
        if start>destination:
            for i in range(start-1,destination-1,-1):
                sum+=distance[i]
        else:
            for i in range(start,destination):
                sum+=distance[i]
        for i in range(len(distance)):
            _all+=distance[i]
        result=min(sum,_all-sum)
        return result
        