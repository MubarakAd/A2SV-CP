class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        my_dict=defaultdict(int)
        left=0
        right=0
        maxx=float("-inf")
        flag=False

        while right<len(nums):
            my_dict[nums[right]]+=1
         
            if my_dict[nums[right]]>1 and nums[right]==0:
                flag=True
                while my_dict[nums[right]]>1:
                    my_dict[nums[left]]-=1
                    left+=1
               
            right+=1
            maxx=max(maxx,right-left)
            
        return maxx-1

        