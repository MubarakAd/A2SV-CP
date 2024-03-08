class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left,right=0,max(nums)
        ans=0
        while left<=right:
            _sum=0
            mid=(right+left)//2
            if mid==0:
                left=1
                continue
            for i in range(len(nums)):
                _sum+=ceil(nums[i]/mid)
            if _sum<=threshold:
                ans=mid
                right=mid-1    
            else:
                left=mid+1
        return ans

        