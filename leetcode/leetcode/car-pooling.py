class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxx=float("-inf")
        minn=float("inf")
        for i in trips:
            maxx=max(i[2],maxx)
            minn=min(minn,i[1])
        entire_trips=[0]*(maxx+1)
        for numP,start,end in  trips:
            entire_trips[start]+=numP
            entire_trips[end]-=numP
        _sum=0
        for i in range(len(entire_trips)):
            _sum+=entire_trips[i]
            entire_trips[i]=_sum
        for i in entire_trips:
            if i>capacity:
                return False
        return True
            


        