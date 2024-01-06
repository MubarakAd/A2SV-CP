class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count=0
        costs.sort()
        for i in costs:
            if coins<i:
                break
            else:
                count+=1
                coins-=i
        return count

        