class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        right=k
        maxx=float("-inf")
        _sum=sum(nums[left:right])
        maxx=max(_sum,maxx)
        while right<len(nums):
                _sum-=nums[left]
                _sum+=nums[right]
                maxx=max(_sum,maxx)
                left+=1
                right+=1
        maxx=maxx/k
        return float("{:.5f}".format(maxx))
            

        