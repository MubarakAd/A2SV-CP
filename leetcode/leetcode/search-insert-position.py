class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x=bisect_left(nums,target)
        return x
        