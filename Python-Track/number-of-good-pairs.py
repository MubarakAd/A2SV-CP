class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        left=0
        right=1
        count=0
        while left<=len(nums)-2:
            if right<=len(nums)-1 and nums[left]==nums[right]:
                count+=1
                right+=1
            else:
                if right>=len(nums)-1:
                    left+=1
                    right=left+1
                else:
                    right+=1
        return count
                
                
            
        