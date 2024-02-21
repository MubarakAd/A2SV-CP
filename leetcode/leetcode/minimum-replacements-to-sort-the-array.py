class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0
        num_replacement=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=nums[i+1]:
                continue
            num_replacement=ceil(nums[i]/nums[i+1])
            ans+=num_replacement-1
            nums[i]=nums[i]//num_replacement
        return ans
        