# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range (len(stones)):
            stones[i]=stones[i]*(-1)
        heapq.heapify(stones)

        while len(stones)>1:
            x=heappop(stones)
            y=heappop(stones)
            if x==y:
                continue
            else:
                if x<y:
                    p=x-y
                else:
                    p=y-x
                heappush(stones,p)
        if len(stones)>0:
            return stones[0]*(-1)
        return 0


      
    