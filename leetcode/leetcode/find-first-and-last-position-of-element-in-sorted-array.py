class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x=bisect_left(nums,target)
        y=bisect_right(nums,target)
        if x>len(nums)-1 or (len(nums)!=0 and nums[x]!=target):
            x=-1
        if  y-1 > len(nums)-1 or (len(nums)!=0 and nums[y-1]!=target):
            y=0
        return [x,y-1]
        