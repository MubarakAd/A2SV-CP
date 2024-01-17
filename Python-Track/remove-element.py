class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left=0
        right=0
        while right<len(nums):
            if nums[right]==val:
                nums.remove(nums[right])
            else:
                right+=1
        return len(nums)

        