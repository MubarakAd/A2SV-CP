class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left=0
        right=1
        l=[]

        while right<len(nums)-1:
            if nums[right]+nums[right+1]>nums[left]:
                l.append(sum(nums[left:right+2]))
                left+=1
                right+=1
            left+=1
            right+=1
        if len(l)==0:
            return 0
        else:
            return max(l)
            
        