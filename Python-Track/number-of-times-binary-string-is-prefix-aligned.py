class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxx=float("-inf")
        count=0
        for i in range(len(flips)):
            maxx=max(maxx,flips[i])
            if i+1>=maxx and i+1>=flips[i]:
                count+=1
            
        return count
            
        