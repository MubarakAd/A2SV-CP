class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        min_=float("inf")
        if nums[left]<nums[right]:
            return nums[left]
       
        while left<=right:
             mid=(right+left)//2
             
             if nums[mid]<=nums[right]:
                min_=min(nums[mid],min_)
                right=mid-1
             elif nums[mid]>nums[right]:
                left=mid+1 
             
            
        return min_
        