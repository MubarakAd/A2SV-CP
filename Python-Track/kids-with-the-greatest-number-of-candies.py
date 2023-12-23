class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        maxx=0
        for i in candies:
            maxx=max(maxx,i)
        for i in candies:
            if i+extraCandies>=maxx:
                l.append(True)
            else:
                l.append(False)
        return l
           