class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        my_dict=defaultdict(int)
        left=0
        right=0
        maxx=float("-inf")
        while right<len(nums):
            my_dict[nums[right]]+=1
            if my_dict[nums[right]]>k and nums[right]==0:
                while my_dict[nums[right]]>k:
                    my_dict[nums[left]]-=1
                    left+=1
            right+=1
            maxx=max(maxx,right-left) 
        return maxx

        