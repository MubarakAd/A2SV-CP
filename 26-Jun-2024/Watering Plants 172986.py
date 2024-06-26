# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        temp=capacity
        count=1
        left=0
        right=1
        while right<len(plants):
            if capacity-plants[left]>=plants[right]:
                capacity-=plants[left]
                count+=1
                left+=1
                right+=1
            else:
                count+=(right*2+1)
                right+=1
                left+=1
                capacity=temp
        return count
        