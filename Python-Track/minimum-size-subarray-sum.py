class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minn=float("inf")
        left=0
        right=0
        _sum=0
        flag=False
        while right<len(nums):
            _sum+=nums[right]
            if _sum<target:
                right+=1
            else:
                while _sum>=target:
                    minn=min(minn,right-left+1)
                    flag=True
                    _sum-=nums[left]
                    left+=1 
                right+=1
        if flag:
            return minn
        else:
            return 0
            
        