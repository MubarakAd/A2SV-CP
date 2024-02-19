class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step=float("-inf")
        for i in range(len(nums)):
            max_step=max(max_step-1,nums[i])
            if max_step<=0 and i<len(nums)-1:
                print(max_step)
                return False
        return True
            

        
        
        