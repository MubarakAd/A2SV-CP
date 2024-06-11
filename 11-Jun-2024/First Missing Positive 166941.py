# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        store=set(nums)
        nums.sort()
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=-1*nums[i]
        for i in range(max(nums)):
            if i!=0 and i not in store:
                return i
        return nums[len(nums)-1]+1

        