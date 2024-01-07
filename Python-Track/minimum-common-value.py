class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums=list(set(nums1)&set(nums2))
        if len(nums)!=0:
            nums.sort()
            return nums[0]
        else:
            return -1
        
        