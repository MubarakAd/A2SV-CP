class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref=[0]*len(nums)
        _sum=0
        max_sum=float("-inf")
        for i in range(len(nums)):
            _sum+=nums[i]
            pref[i]=_sum
            max_sum=max(pref[i],max_sum)
            if _sum<0:
                _sum=0
        return max_sum

        