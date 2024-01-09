class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
       ans=[]
       for i in range(len(nums)):
           index=bisect.bisect_left(ans,nums[i])
           
           if index==len(ans):
               ans.append(nums[i])
           else:
                ans[index]=nums[i]
           
           
       if len(ans)>=3:
            return True
       else:
            return False
            
        