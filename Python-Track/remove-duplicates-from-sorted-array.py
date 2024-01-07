class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=1
        while right<=len(nums)-1:
            if nums[left]==nums[right]:
                nums.remove(nums[right])
                
            else:
                right+=1
                left+=1
        return len(nums)