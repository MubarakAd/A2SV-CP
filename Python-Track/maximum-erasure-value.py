class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left=right=_sum=0
        my_dict=defaultdict(int)
        maxx=float("-inf")
        while right<len(nums):
            my_dict[nums[right]]+=1
            _sum+=nums[right]
            if my_dict[nums[right]]<=1:
                right+=1
            else:
                while my_dict[nums[right]]>1:
                    my_dict[nums[left]]-=1
                    _sum-=nums[left]
                    left+=1
                right+=1
            maxx=max(maxx,_sum)
        return maxx


        