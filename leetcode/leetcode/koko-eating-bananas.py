class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        best=len(piles)
       
        while left<=right:
            mid=(left+right)//2
            counter=0
            
            for i in range(len(piles)):
                counter+= ceil(piles[i]/mid)
            if counter>h:
                left=mid+1
            else:
                right=mid-1
                best=mid
        return best
        
            

