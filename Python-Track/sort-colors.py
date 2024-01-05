class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]>nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        
        """
        Do not return anything, modify nums in-place instead.
        """
        