# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i,j=1,n
        min_=float("inf")
        while i<=j:
            mid=(i+j)//2
            if isBadVersion(mid):
                min_=min(mid,min_)
                j=mid-1
            else :
                i=mid+1
            
                
        return min_


        